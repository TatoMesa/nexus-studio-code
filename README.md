# Nexus Studio Code — Sitio Corporativo

Sitio web corporativo profesional desarrollado con Django 5, Bootstrap 5 y diseño oscuro moderno.

## Stack Tecnológico
- **Backend:** Django 5 + Python 3.11+
- **Frontend:** Bootstrap 5, CSS3, JavaScript vanilla
- **Base de datos:** SQLite (dev) / PostgreSQL (prod)
- **Imágenes:** Pillow
- **Admin:** Django Admin personalizado

## Instalación rápida

```bash
# 1. Clonar / descomprimir el proyecto
cd nexus_studio_code

# 2. Entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migraciones
python manage.py migrate

# 5. Superusuario admin
python manage.py createsuperuser

# 6. Cargar datos de ejemplo (opcional)
python manage.py loaddata fixtures/demo.json

# 7. Servidor de desarrollo
python manage.py runserver
```

## Acceso al Admin
- URL: http://localhost:8000/admin/
- Demo: admin / nexus2025

## Estructura del Proyecto
```
nexus_studio_code/
├── config/          # Configuración Django
├── core/            # App principal (servicios, tecnologías, estadísticas, etc.)
├── portfolio/       # App de proyectos
├── contact/         # App de contacto
├── templates/       # Templates HTML
├── static/          # CSS, JS, imágenes
├── media/           # Uploads (imágenes de proyectos, etc.)
└── manage.py
```

## Administración de Contenido
Todo se administra desde `/admin/` sin tocar código:
- **SiteConfig:** logo, textos hero, about, contacto, SEO
- **Services:** servicios con íconos Bootstrap
- **Technology:** tecnologías con colores personalizados
- **Statistic:** métricas animadas
- **Testimonial:** testimonios de clientes
- **Project:** portafolio con imágenes, URLs, tecnologías
- **SocialLink:** redes sociales del footer
- **ContactMessage:** consultas recibidas del formulario

## Para producción (PostgreSQL)
En `config/settings.py` cambiar DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nexus_db',
        'USER': 'nexus_user',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
