from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+54 11 1234-5678'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Cuéntanos sobre tu proyecto...'}),
        }
        labels = {
            'name': 'Nombre completo',
            'email': 'Email',
            'phone': 'Teléfono (opcional)',
            'message': 'Mensaje',
        }
