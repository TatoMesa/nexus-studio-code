# Nexus Studio Code — Plataforma Web Corporativa (Software Factory)

Plataforma web empresarial de alto rendimiento desarrollada con **Django 5**, **Bootstrap 5**, **CSS3 Neon Glassmorphism** y **JavaScript Vanilla**, optimizada para la captación, cotización y conversión de clientes corporativos para una empresa de desarrollo de software a medida.

---

## 🚀 Características Principales

1. **Cotizador Interactivo de Proyectos (Lead Magnet)**:
   - Estimación de inversión y plazos de entrega en tiempo real según tipo de solución, módulos técnicos y urgencia.
   - Envío asíncrono (AJAX) y almacenamiento directo en base de datos (`QuoteRequest`).
2. **Hero Interactivo con IDE de Código**:
   - Selector de pestañas de archivos (`app/api.py`, `models/saas.py`, `deploy.json`) con sintaxis resaltada y botón para copiar código.
   - Badges flotantes con micro-animaciones (NDA garantizado, entregas en sprints, 99.9% uptime).
3. **Secciones Estratégicas B2B**:
   - **Metodología de Trabajo por Fases**: Discovery & Sprint 0 ➔ UX/UI ➔ Sprints Ágiles ➔ QA & Seguridad ➔ Despliegue & Soporte 24/7.
   - **Stack Tecnológico Organizado por Capas**: Backend, Frontend, Bases de Datos, Cloud & DevOps e Inteligencia Artificial.
   - **Garantías Contractuales**: 100% propiedad del código fuente, Acuerdos de Confidencialidad (NDA) y precios cerrados por sprint.
   - **Acordeón Interactivo de Preguntas Frecuentes (FAQ)**.
4. **Portafolio Enriquecido (Casos de Estudio)**:
   - Filtros dinámicos por categoría (SaaS, ERP, APIs, Web Apps, Mobile).
   - Vista de caso de estudio detallada: *Problema del Cliente ➔ Solución Técnica ➔ Arquitectura ➔ Métricas y Resultados Obtenidos*.
5. **Canales de Conversión Rápida**:
   - Botón flotante inteligente de WhatsApp con mensaje contextual y efecto pulse.
   - Página dedicada de contacto profesional en `/contacto/`.
6. **Panel de Control Django Admin 100% Dinámico**:
   - Gestión integral de servicios, tecnologías, testimonios, cotizaciones recibidas, FAQs y configuración SEO.
7. **Sembrado Automático de Datos**:
   - Comando `python manage.py seed_company_data` con datos comerciales completos de muestra.

---

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.11+ / 3.13, Django 5.x
- **Gestión de Configuración:** `python-decouple` con soporte para `.env`
- **Frontend:** Vanilla CSS3 (variables HSL dinámicas), JavaScript Vanilla, Bootstrap 5.3.3, Bootstrap Icons
- **Tipografías:** Space Grotesk & JetBrains Mono (Google Fonts)
- **Base de datos:** SQLite (desarrollo local) / PostgreSQL (producción)
- **Archivos Estáticos:** WhiteNoise con compresión y caché de manifiesto
- **SEO:** Marcado estructurado Schema.org JSON-LD, OpenGraph, `sitemap.xml` y `robots.txt`

---

## 📦 Instalación y Puesta en Marcha

```bash
# 1. Acceder al directorio del proyecto
cd nexus_studio_code

# 2. Crear y activar entorno virtual
# En Windows:
py -3.13 -m venv venv_win
.\venv_win\Scripts\activate

# En Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env

# 5. Ejecutar migraciones
python manage.py migrate

# 6. Sembrar datos corporativos profesionales
python manage.py seed_company_data

# 7. Crear superusuario para el panel de administración
python manage.py createsuperuser

# 8. Iniciar el servidor de desarrollo
python manage.py runserver
```

---

## 🧭 Estructura del Proyecto

```
nexus_studio_code/
├── config/              # Configuración global Django (settings, urls, wsgi, asgi)
├── core/                # Aplicación principal (Home, Cotizador, Servicios, Metodología, Stack, FAQ)
│   ├── management/
│   │   └── commands/
│   │       └── seed_company_data.py # Comando de inicialización de datos
│   ├── models.py        # Modelos (SiteConfig, Service, Technology, ProcessStep, FAQ, QuoteRequest)
│   └── views.py         # Controladores de Home y API de Cotización
├── portfolio/           # Aplicación de Portafolio y Casos de Estudio
│   ├── models.py        # Modelo Project con métricas, desafío y solución
│   └── views.py         # Listado con filtros y detalle de caso de estudio
├── contact/             # Aplicación de Contacto dedicada
│   ├── forms.py         # Formulario de contacto
│   ├── models.py        # Modelo ContactMessage
│   └── views.py         # Vista dedicada /contacto/
├── templates/           # Plantillas HTML optimizadas
│   ├── base.html        # Plantilla base con navbar, widget WhatsApp, Schema.org y footer
│   ├── core/home.html   # Landing page completa con cotizador y secciones interactivas
│   ├── portfolio/       # Plantillas list.html y detail.html
│   └── contact/         # Plantilla contact.html
├── static/              # Archivos estáticos
│   ├── css/main.css     # Hoja de estilos con Glassmorphism y temas HSL
│   ├── js/main.js       # Motor de cálculo del cotizador, IDE tabs y animaciones
│   └── images/          # Logotipos y recursos visuales
├── media/               # Carga de imágenes dinámicas desde el admin
├── .env.example         # Plantilla de variables de entorno
├── requirements.txt     # Dependencias de producción
└── manage.py
```

---

## 🔐 Panel Administrativo (`/admin/`)

- URL: `http://127.0.0.1:8000/admin/`
- Gestión de:
  - **Cotizaciones de Proyectos**: Visualiza solicitudes enviadas por el cotizador con presupuesto, módulos y datos del cliente.
  - **Consultas de Contacto**: Mensajes recibidos con IP y estado.
  - **Metodología & FAQs**: Edita y agrega pasos del proceso o preguntas frecuentes.
  - **Servicios & Tecnologías**: Personaliza servicios, colores de íconos y categorías.
  - **Configuración del Sitio**: Nombre, logo, eslogan, número de WhatsApp y SEO.

