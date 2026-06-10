from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('contact:contact')
    return render(request, 'contact/contact.html', {'form': form})
