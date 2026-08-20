from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from core.models import SiteConfig, FAQ, SocialLink


def contact(request):
    config = SiteConfig.get_config()
    faqs = FAQ.objects.filter(is_active=True, category__in=['general', 'payment'])[:4]
    social_links = SocialLink.objects.filter(is_active=True)
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                contact_msg.ip_address = x_forwarded_for.split(',')[0]
            else:
                contact_msg.ip_address = request.META.get('REMOTE_ADDR')
            contact_msg.save()

            try:
                send_mail(
                    subject=f'[Contacto Web] Mensaje de {contact_msg.name}',
                    message=f'Nombre: {contact_msg.name}\nEmail: {contact_msg.email}\nTeléfono: {contact_msg.phone}\n\nMensaje:\n{contact_msg.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[config.email],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, '¡Tu mensaje ha sido enviado exitosamente! Nos contactaremos contigo a la brevedad.')
            return redirect('contact:contact')

    context = {
        'form': form,
        'config': config,
        'faqs': faqs,
        'social_links': social_links,
        'page_title': f'Contacto & Asesoría — {config.company_name}',
    }
    return render(request, 'contact/contact.html', context)

