from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completado'),
        ('in_progress', 'En Progreso'),
        ('maintenance', 'En Mantenimiento'),
    ]
    title = models.CharField('Título', max_length=150)
    slug = models.SlugField('Slug', unique=True, blank=True)
    description = models.TextField('Descripción')
    short_description = models.CharField('Descripción corta', max_length=200, blank=True)
    image = models.ImageField('Imagen principal', upload_to='projects/')
    technologies = models.CharField('Tecnologías', max_length=300, help_text='Ej: Python, Django, PostgreSQL')
    public_url = models.URLField('URL pública', blank=True)
    github_url = models.URLField('Repositorio GitHub', blank=True)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default='completed')
    is_featured = models.BooleanField('Destacado', default=False)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]
