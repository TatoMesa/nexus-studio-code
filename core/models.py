from django.db import models


class SiteConfig(models.Model):
    company_name = models.CharField('Nombre de la empresa', max_length=100, default='Nexus Studio Code')
    tagline = models.CharField('Eslogan', max_length=200, default='Transformamos ideas en soluciones digitales')
    hero_title = models.CharField('Título Hero', max_length=200, default='Desarrollo de Software a Medida')
    hero_subtitle = models.TextField('Subtítulo Hero', default='Creamos soluciones tecnológicas innovadoras que impulsan tu negocio al siguiente nivel.')
    about_history = models.TextField('Historia', blank=True)
    about_mission = models.TextField('Misión', blank=True)
    about_vision = models.TextField('Visión', blank=True)
    about_values = models.TextField('Valores', blank=True)
    email = models.EmailField('Email principal', default='info@nexusstudiocode.com')
    phone = models.CharField('Teléfono', max_length=30, blank=True)
    address = models.CharField('Dirección', max_length=200, blank=True)
    logo = models.ImageField('Logo', upload_to='site/', blank=True, null=True)
    favicon = models.ImageField('Favicon', upload_to='site/', blank=True, null=True)
    meta_description = models.TextField('Meta descripción SEO', blank=True, max_length=160)
    meta_keywords = models.CharField('Keywords SEO', max_length=300, blank=True)
    google_analytics = models.CharField('Google Analytics ID', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Configuración del Sitio'
        verbose_name_plural = 'Configuración del Sitio'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_config(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Service(models.Model):
    ICON_CHOICES = [
        ('bi-globe', 'Desarrollo Web'),
        ('bi-gear-fill', 'Sistemas de Gestión'),
        ('bi-cpu', 'Automatización'),
        ('bi-server', 'APIs y Backend'),
        ('bi-plug', 'Integraciones'),
        ('bi-lightbulb', 'Consultoría'),
        ('bi-phone', 'Mobile'),
        ('bi-shield-check', 'Seguridad'),
        ('bi-graph-up', 'Analytics'),
        ('bi-cloud', 'Cloud'),
    ]
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descripción')
    icon = models.CharField('Ícono Bootstrap', max_length=50, choices=ICON_CHOICES, default='bi-globe')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)
    highlight = models.BooleanField('Destacado', default=False)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class Technology(models.Model):
    name = models.CharField('Nombre', max_length=50)
    icon_class = models.CharField('Clase CSS del ícono', max_length=100, blank=True, help_text='Clase devicon o similar')
    icon_svg = models.TextField('SVG del ícono', blank=True)
    color = models.CharField('Color hex', max_length=10, default='#00ff88')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Statistic(models.Model):
    label = models.CharField('Etiqueta', max_length=100)
    value = models.PositiveIntegerField('Valor numérico')
    suffix = models.CharField('Sufijo', max_length=10, blank=True, default='+')
    icon = models.CharField('Ícono Bootstrap', max_length=50, default='bi-trophy')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Estadística'
        verbose_name_plural = 'Estadísticas'
        ordering = ['order']

    def __str__(self):
        return f'{self.label}: {self.value}{self.suffix}'


class Testimonial(models.Model):
    client_name = models.CharField('Nombre del cliente', max_length=100)
    client_position = models.CharField('Cargo', max_length=100, blank=True)
    client_company = models.CharField('Empresa', max_length=100, blank=True)
    client_photo = models.ImageField('Foto', upload_to='testimonials/', blank=True, null=True)
    message = models.TextField('Testimonio')
    rating = models.PositiveIntegerField('Calificación (1-5)', default=5)
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.client_name} — {self.client_company}'


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter/X'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('facebook', 'Facebook'),
        ('whatsapp', 'WhatsApp'),
    ]
    platform = models.CharField('Red social', max_length=30, choices=PLATFORM_CHOICES)
    url = models.URLField('URL')
    is_active = models.BooleanField('Activo', default=True)
    order = models.PositiveIntegerField('Orden', default=0)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['order']

    def __str__(self):
        return self.platform

    def get_icon(self):
        icons = {
            'github': 'bi-github',
            'linkedin': 'bi-linkedin',
            'twitter': 'bi-twitter-x',
            'instagram': 'bi-instagram',
            'youtube': 'bi-youtube',
            'facebook': 'bi-facebook',
            'whatsapp': 'bi-whatsapp',
        }
        return icons.get(self.platform, 'bi-link')
