from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completado'),
        ('in_progress', 'En Desarrollo'),
        ('maintenance', 'Producción & Mantenimiento'),
    ]
    CATEGORY_CHOICES = [
        ('all', 'Todos'),
        ('web', 'Web App & SaaS'),
        ('erp', 'Sistemas de Gestión / ERP'),
        ('mobile', 'App Móvil'),
        ('api', 'APIs & Backend'),
        ('ai', 'Automatización & IA'),
    ]
    title = models.CharField('Título', max_length=150)
    slug = models.SlugField('Slug', unique=True, blank=True)
    category = models.CharField('Categoría', max_length=20, choices=CATEGORY_CHOICES, default='web')
    client_name = models.CharField('Cliente / Industria', max_length=120, blank=True, help_text='Ej: FinTech, E-commerce, Logística')
    short_description = models.CharField('Descripción corta', max_length=250, blank=True)
    description = models.TextField('Descripción general')
    
    # Caso de estudio
    challenge = models.TextField('Desafío / Problema del cliente', blank=True, help_text='¿Qué problema u objetivo tenía el cliente?')
    solution = models.TextField('Solución técnica implementada', blank=True, help_text='¿Cómo lo resolvimos con arquitectura y software?')
    results = models.TextField('Resultados / Métricas de impacto', blank=True, help_text='Ej: 40% reducción en tiempos operativos, 10k usuarios activos')
    
    image = models.ImageField('Imagen principal', upload_to='projects/', blank=True, null=True)
    technologies = models.CharField('Tecnologías', max_length=300, help_text='Ej: Python, Django, PostgreSQL, Docker, React')
    public_url = models.URLField('URL pública / Demo online', blank=True)
    github_url = models.URLField('Repositorio GitHub (opcional)', blank=True)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default='completed')
    is_featured = models.BooleanField('Destacado en Home', default=False)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)
    completion_date = models.CharField('Fecha de entrega / Año', max_length=50, blank=True, default='2025')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Proyecto / Caso de Estudio'
        verbose_name_plural = 'Portafolio de Proyectos'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.title} ({self.get_category_display()})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_results_list(self):
        if not self.results:
            return []
        return [r.strip() for r in self.results.split('\n') if r.strip()]

