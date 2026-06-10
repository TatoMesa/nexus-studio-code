from django.db import models


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nuevo'),
        ('read', 'Leído'),
        ('replied', 'Respondido'),
        ('archived', 'Archivado'),
    ]
    name = models.CharField('Nombre', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Teléfono', max_length=30, blank=True)
    message = models.TextField('Mensaje')
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default='new')
    ip_address = models.GenericIPAddressField('IP', blank=True, null=True)
    created_at = models.DateTimeField('Fecha', auto_now_add=True)

    class Meta:
        verbose_name = 'Consulta de Contacto'
        verbose_name_plural = 'Consultas de Contacto'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.email} ({self.created_at.strftime("%d/%m/%Y")})'
