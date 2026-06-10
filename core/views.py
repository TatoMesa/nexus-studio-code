from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SiteConfig, Service, Technology, Statistic, Testimonial, SocialLink
from portfolio.models import Project
from contact.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    config = SiteConfig.get_config()
    services = Service.objects.filter(is_active=True)
    technologies = Technology.objects.filter(is_active=True)
    stats = Statistic.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    featured_projects = Project.objects.filter(is_active=True, is_featured=True)[:6]
    social_links = SocialLink.objects.filter(is_active=True)

    form = ContactForm()
    if request.method == 'POST':
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
                    subject=f'Nueva consulta de {contact.name}',
                    message=f'Nombre: {contact.name}\nEmail: {contact.email}\nTeléfono: {contact.phone}\n\nMensaje:\n{contact.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[config.email],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, '¡Mensaje enviado! Te contactaremos pronto.')
            form = ContactForm()

    context = {
        'config': config,
        'services': services,
        'technologies': technologies,
        'stats': stats,
        'testimonials': testimonials,
        'featured_projects': featured_projects,
        'social_links': social_links,
        'form': form,
        'page_title': f'{config.company_name} — Desarrollo de Software a Medida',
    }
    return render(request, 'core/home.html', context)
