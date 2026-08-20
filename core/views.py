import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    SiteConfig, Service, Technology, ProcessStep,
    ValueProposition, FAQ, Statistic, Testimonial,
    SocialLink, QuoteRequest
)
from portfolio.models import Project
from contact.forms import ContactForm


def home(request):
    config = SiteConfig.get_config()
    services = Service.objects.filter(is_active=True)
    all_technologies = Technology.objects.filter(is_active=True)
    
    # Agrupar tecnologías por categorías para las pestañas interactivas
    tech_categories = {
        'backend': all_technologies.filter(category='backend'),
        'frontend': all_technologies.filter(category='frontend'),
        'database': all_technologies.filter(category='database'),
        'cloud': all_technologies.filter(category='cloud'),
        'ai': all_technologies.filter(category='ai'),
    }

    process_steps = ProcessStep.objects.filter(is_active=True)
    value_props = ValueProposition.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    stats = Statistic.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    featured_projects = Project.objects.filter(is_active=True, is_featured=True)[:6]
    social_links = SocialLink.objects.filter(is_active=True)

    form = ContactForm()
    if request.method == 'POST' and 'contact_submit' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                contact.ip_address = x_forwarded_for.split(',')[0]
            else:
                contact.ip_address = request.META.get('REMOTE_ADDR')
            contact.save()
            try:
                send_mail(
                    subject=f'[Web Consulta] Nuevo mensaje de {contact.name}',
                    message=f'Nombre: {contact.name}\nEmail: {contact.email}\nTeléfono: {contact.phone}\n\nMensaje:\n{contact.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[config.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, '¡Mensaje recibido con éxito! Nos comunicaremos contigo en menos de 24 horas hábiles.')
            return redirect('core:home')

    context = {
        'config': config,
        'services': services,
        'technologies': all_technologies,
        'tech_categories': tech_categories,
        'process_steps': process_steps,
        'value_props': value_props,
        'faqs': faqs,
        'stats': stats,
        'testimonials': testimonials,
        'featured_projects': featured_projects,
        'social_links': social_links,
        'form': form,
        'page_title': f'{config.company_name} — {config.tagline}',
    }
    return render(request, 'core/home.html', context)


@require_POST
def quote_request(request):
    """Endpoint para procesar solicitudes del Cotizador Interactivo de Presupuestos"""
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json'
    
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
        except Exception:
            data = {}
    else:
        data = request.POST

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    company = data.get('company', '').strip()
    project_type = data.get('project_type', '').strip()
    features = data.get('features', '')
    if isinstance(features, list):
        features = ', '.join(features)
    budget_range = data.get('budget_range', '').strip()
    timeline = data.get('timeline', '').strip()
    description = data.get('description', '').strip()
    estimated_cost = data.get('estimated_cost', '').strip()

    # Validación básica
    if not name or not email or not project_type:
        if is_ajax:
            return JsonResponse({'status': 'error', 'message': 'Por favor completa nombre, email y tipo de proyecto.'}, status=400)
        messages.error(request, 'Por favor completa los campos obligatorios del cotizador.')
        return redirect('core:home')

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    quote = QuoteRequest.objects.create(
        name=name,
        email=email,
        phone=phone,
        company=company,
        project_type=project_type,
        features=features,
        budget_range=budget_range,
        timeline=timeline,
        description=description,
        estimated_cost_display=estimated_cost,
        ip_address=ip,
        status='new'
    )

    config = SiteConfig.get_config()
    try:
        send_mail(
            subject=f'[Nueva Cotización #{quote.id}] {project_type} — {name}',
            message=(
                f'Solicitud de Cotización #{quote.id}\n'
                f'------------------------------------\n'
                f'Cliente: {name}\n'
                f'Email: {email}\n'
                f'Teléfono: {phone}\n'
                f'Empresa: {company}\n'
                f'Tipo de Proyecto: {project_type}\n'
                f'Funcionalidades: {features}\n'
                f'Plazo deseado: {timeline}\n'
                f'Cálculo Estimado Web: {estimated_cost}\n'
                f'Detalles adicionales:\n{description}\n'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[config.email],
            fail_silently=True,
        )
    except Exception:
        pass

    success_msg = f'¡Excelente {name}! Hemos recibido tu solicitud de cotización para {project_type}. En breve un arquitecto de software te enviará la propuesta detallada.'

    if is_ajax:
        return JsonResponse({
            'status': 'ok',
            'message': success_msg,
            'quote_id': quote.id
        })

    messages.success(request, success_msg)
    return redirect('core:home')

