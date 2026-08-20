import re
from urllib.parse import quote
from django.db import models


class SiteConfig(models.Model):
    company_name = models.CharField('Nombre de la empresa', max_length=100, default='Nexus Studio Code')
    tagline = models.CharField('Eslogan', max_length=200, default='Transformamos ideas en soluciones digitales escalables')
    hero_badge_text = models.CharField('Texto Badge Hero', max_length=100, default='Disponibles para nuevos proyectos')
    hero_title = models.CharField('Título Hero', max_length=200, default='Desarrollo de Software a Medida de Alto Impacto')
    hero_subtitle = models.TextField('Subtítulo Hero', default='Diseñamos y desarrollamos plataformas web, aplicaciones SaaS, APIs robustas y sistemas de gestión de alto rendimiento para empresas y startups.')
    experience_years = models.CharField('Años de experiencia', max_length=10, default='5+')
    
    about_history = models.TextField('Historia', blank=True)
    about_mission = models.TextField('Misión', blank=True)
    about_vision = models.TextField('Visión', blank=True)
    about_values = models.TextField('Valores', blank=True)
    
    email = models.EmailField('Email principal', default='contacto@nexusstudiocode.online')
    phone = models.CharField('Teléfono / WhatsApp Visible', max_length=30, blank=True, default='+54 9 11 5555-0199', help_text='Ej: +54 9 249 466-8517')
    whatsapp_number = models.CharField('Número de WhatsApp para enlaces (con código de país)', max_length=60, blank=True, default='5491155550199', help_text='Ej: 5492494668517 (se limpian símbolos y espacios automáticamente)')
    whatsapp_message = models.CharField('Mensaje predeterminado de WhatsApp', max_length=250, blank=True, default='Hola Nexus Studio Code, me gustaría consultar por el desarrollo de un proyecto de software.')
    meeting_url = models.URLField('URL para agendar reunión (Calendly/Meet)', blank=True)
    address = models.CharField('Dirección / Ubicación', max_length=200, blank=True, default='Buenos Aires, Argentina (Servicios Globales)')
    
    logo = models.ImageField('Logo', upload_to='site/', blank=True, null=True)
    favicon = models.ImageField('Favicon', upload_to='site/', blank=True, null=True)
    meta_description = models.TextField('Meta descripción SEO', blank=True, max_length=160, default='Empresa de desarrollo de software a medida, aplicaciones web, SaaS, APIs y modernización de sistemas empresariales.')
    meta_keywords = models.CharField('Keywords SEO', max_length=300, blank=True, default='desarrollo software a medida, software factory, python, django, react, saas, apis, argentina')
    google_analytics = models.CharField('Google Analytics ID', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Configuración del Sitio'
        verbose_name_plural = 'Configuración del Sitio'

    def __str__(self):
        return self.company_name

    @property
    def clean_whatsapp_number(self):
        """Retorna solo los dígitos para armar URLs wa.me/"""
        if self.whatsapp_number:
            digits = re.sub(r'\D', '', str(self.whatsapp_number))
            if digits:
                return digits
        # Fallback a SocialLink
        try:
            wa_social = SocialLink.objects.filter(platform='whatsapp', is_active=True).first()
            if wa_social and wa_social.url:
                digits = re.sub(r'\D', '', str(wa_social.url))
                if digits:
                    return digits
        except Exception:
            pass
        return ''

    def get_whatsapp_url(self, custom_message=None):
        """Genera el enlace completo wa.me con mensaje codificado"""
        number = self.clean_whatsapp_number
        if not number:
            return '#'
        msg = custom_message if custom_message is not None else self.whatsapp_message
        if msg:
            return f"https://wa.me/{number}?text={quote(msg)}"
        return f"https://wa.me/{number}"

    def save(self, *args, **kwargs):
        self.pk = 1
        # Si el usuario ingresó un link o formato con símbolos, limpiar a solo dígitos
        if self.whatsapp_number:
            digits = re.sub(r'\D', '', str(self.whatsapp_number))
            if digits:
                self.whatsapp_number = digits
        super().save(*args, **kwargs)

        # Sincronizar automáticamente con SocialLink para que el footer siempre coincida
        try:
            number = self.clean_whatsapp_number
            if number:
                wa_link, _ = SocialLink.objects.get_or_create(platform='whatsapp', defaults={'order': 3, 'is_active': True})
                wa_url = f"https://wa.me/{number}"
                if wa_link.url != wa_url:
                    SocialLink.objects.filter(pk=wa_link.pk).update(url=wa_url)
        except Exception:
            pass

    @classmethod
    def get_config(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj



class Service(models.Model):
    ICON_CHOICES = [
        ('bi-globe', 'Desarrollo Web & SaaS'),
        ('bi-gear-fill', 'Sistemas de Gestión / ERP / CRM'),
        ('bi-cpu', 'Automatización & IA'),
        ('bi-server', 'APIs & Arquitectura Backend'),
        ('bi-plug', 'Integraciones & Microservicios'),
        ('bi-lightbulb', 'Consultoría Tecnológica & Sprint 0'),
        ('bi-phone', 'Aplicaciones Móviles'),
        ('bi-shield-check', 'Auditoría & Seguridad'),
        ('bi-cloud-check', 'DevOps & Cloud (AWS/Docker)'),
        ('bi-database-check', 'Bases de Datos & Data Engineering'),
    ]
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descripción')
    features_list = models.TextField('Características clave (1 por línea)', blank=True, help_text='Separar cada punto con un salto de línea')
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

    def get_features(self):
        if not self.features_list:
            return []
        return [f.strip() for f in self.features_list.split('\n') if f.strip()]


class Technology(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend & APIs'),
        ('frontend', 'Frontend & UI/UX'),
        ('database', 'Bases de Datos'),
        ('cloud', 'Cloud, DevOps & Infraestructura'),
        ('ai', 'IA & Automatización'),
    ]
    name = models.CharField('Nombre', max_length=50)
    category = models.CharField('Categoría', max_length=20, choices=CATEGORY_CHOICES, default='backend')
    icon_class = models.CharField('Clase CSS del ícono', max_length=100, blank=True, help_text='Clase devicon o bootstrap')
    icon_svg = models.TextField('SVG del ícono', blank=True)
    color = models.CharField('Color hex', max_length=10, default='#00ff88')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Tecnología'
        verbose_name_plural = 'Tecnologías'
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.name} ({self.get_category_display()})'


class ProcessStep(models.Model):
    step_number = models.CharField('Número de Paso (ej: 01)', max_length=5, default='01')
    title = models.CharField('Título', max_length=100)
    subtitle = models.CharField('Subtítulo / Objetivo', max_length=150, blank=True)
    description = models.TextField('Descripción detallada')
    icon = models.CharField('Ícono Bootstrap', max_length=50, default='bi-compass')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Paso de Metodología'
        verbose_name_plural = 'Metodología de Trabajo'
        ordering = ['order', 'step_number']

    def __str__(self):
        return f'{self.step_number}. {self.title}'


class ValueProposition(models.Model):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descripción')
    icon = models.CharField('Ícono Bootstrap', max_length=50, default='bi-shield-check')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Garantía / Diferencial'
        verbose_name_plural = 'Garantías y Diferenciales'
        ordering = ['order']

    def __str__(self):
        return self.title


class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General & Contratación'),
        ('process', 'Metodología & Plazos'),
        ('tech', 'Tecnología & Propiedad Intelectual'),
        ('payment', 'Presupuestos & Pagos'),
    ]
    question = models.CharField('Pregunta', max_length=250)
    answer = models.TextField('Respuesta')
    category = models.CharField('Categoría', max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.PositiveIntegerField('Orden', default=0)
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Pregunta Frecuente'
        verbose_name_plural = 'Preguntas Frecuentes (FAQ)'
        ordering = ['order', 'id']

    def __str__(self):
        return self.question


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.platform == 'whatsapp' and self.url:
            digits = re.sub(r'\D', '', str(self.url))
            if digits:
                try:
                    SiteConfig.objects.filter(pk=1).update(whatsapp_number=digits)
                except Exception:
                    pass



class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nueva'),
        ('in_review', 'En Evaluación'),
        ('contacted', 'Cliente Contactado'),
        ('proposal_sent', 'Propuesta Enviada'),
        ('closed', 'Cerrada / Aceptada'),
        ('rejected', 'Descartada'),
    ]
    name = models.CharField('Nombre y Apellido', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Teléfono / WhatsApp', max_length=40, blank=True)
    company = models.CharField('Empresa / Organización', max_length=120, blank=True)
    project_type = models.CharField('Tipo de Proyecto', max_length=100)
    features = models.TextField('Funcionalidades Requeridas', blank=True)
    budget_range = models.CharField('Rango de Presupuesto Estimado', max_length=100, blank=True)
    timeline = models.CharField('Plazo Estimado', max_length=100, blank=True)
    description = models.TextField('Detalles del Proyecto', blank=True)
    estimated_cost_display = models.CharField('Cálculo Estimado Generado', max_length=100, blank=True)
    ip_address = models.GenericIPAddressField('Dirección IP', blank=True, null=True)
    status = models.CharField('Estado', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Fecha de Solicitud', auto_now_add=True)

    class Meta:
        verbose_name = 'Solicitud de Cotización'
        verbose_name_plural = 'Cotizaciones de Proyectos'
        ordering = ['-created_at']

    def __str__(self):
        return f'Cotización #{self.id}: {self.project_type} — {self.name} ({self.created_at.strftime("%d/%m/%Y")})'

