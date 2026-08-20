from django.core.management.base import BaseCommand
from core.models import (
    SiteConfig, Service, Technology, ProcessStep,
    ValueProposition, FAQ, Statistic, Testimonial, SocialLink
)
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Sembrado de datos profesionales para la empresa Nexus Studio Code'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando sembrado de datos profesionales...'))

        # 1. SiteConfig
        config, _ = SiteConfig.objects.get_or_create(pk=1)
        config.company_name = 'Nexus Studio Code'
        config.tagline = 'Ingeniería de Software & Soluciones Digitales de Alto Impacto'
        config.hero_badge_text = '🚀 Disponibles para nuevos proyectos & sprints'
        config.hero_title = 'Desarrollo de Software a Medida para Empresas y Startups'
        config.hero_subtitle = 'Construimos plataformas web escalables, arquitecturas SaaS, sistemas ERP y APIs de alto rendimiento que aceleran el crecimiento de tu negocio.'
        config.experience_years = '5+'
        config.about_history = 'Nacimos con la visión de cerrar la brecha entre la complejidad tecnológica y los objetivos de negocio. En Nexus Studio Code nos especializamos en transformar ideas ambiciosas y procesos corporativos en productos digitales robustos, elegantes y de nivel mundial.'
        config.about_mission = 'Diseñar y construir software de alta fidelidad técnica que maximice la eficiencia operativa y genere ventajas competitivas reales para nuestros clientes.'
        config.about_vision = 'Consolidarnos como el partner tecnológico de referencia en desarrollo a medida y arquitectura de software para empresas de Latinoamérica y el mundo.'
        config.about_values = 'Excelencia técnica, transparencia absoluta en el código y plazos, obsesión por el rendimiento y compromiso a largo plazo con cada producto que creamos.'
        config.email = 'contacto@nexusstudiocode.com'
        config.phone = '+54 9 11 5555-0199'
        config.whatsapp_number = '5491155550199'
        config.whatsapp_message = 'Hola Nexus Studio Code! Me comunico desde la web para consultar por el desarrollo de un proyecto.'
        config.address = 'Buenos Aires, Argentina (Atención Remota Global)'
        config.meta_description = 'Empresa de desarrollo de software a medida. Especialistas en Python, Django, React, SaaS, APIs y modernización de sistemas empresariales.'
        config.meta_keywords = 'software factory, desarrollo software a medida, aplicaciones web, python, django, react, saas, microservicios, buenos aires, argentina'
        config.save()
        self.stdout.write(self.style.SUCCESS('[OK] Configuracion del sitio actualizada.'))

        # 2. Services
        services_data = [
            {
                'title': 'Desarrollo Web & Plataformas SaaS',
                'description': 'Creamos aplicaciones web complejas, plataformas de suscripción y portales de usuario con arquitecturas modernas, rápidas y seguras.',
                'features_list': 'Arquitectura multi-tenant y escalable\nPaneles de administración a medida\nIntegración de pasarelas de pago y facturación\nOptimización de velocidad y SEO técnico',
                'icon': 'bi-globe',
                'highlight': True,
                'order': 1,
            },
            {
                'title': 'Sistemas de Gestión / ERP & CRM',
                'description': 'Digitalizamos y automatizamos la operación de tu empresa: control de stock, facturación electrónica, RRHH, logística y paneles de métricas.',
                'features_list': 'Módulos adaptados 100% a tu flujo de trabajo\nReportes en tiempo real y exportación de datos\nRoles, permisos granulares y auditoría de acciones\nSincronización con bases de datos heredadas',
                'icon': 'bi-gear-fill',
                'highlight': False,
                'order': 2,
            },
            {
                'title': 'APIs REST & Arquitectura Backend',
                'description': 'Diseño e implementación de microservicios y APIs robustas construidas en Python/Django para conectar aplicaciones móviles, frontends y servicios externos.',
                'features_list': 'Documentación interactiva OpenAPI / Swagger\nAutenticación JWT, OAuth2 y rate limiting\nProcesamiento asíncrono con Celery y Redis\nAlta concurrencia y baja latencia',
                'icon': 'bi-server',
                'highlight': False,
                'order': 3,
            },
            {
                'title': 'Automatización & Soluciones con IA',
                'description': 'Optimizamos tareas repetitivas conectando tus sistemas con modelos de lenguaje (LLMs), agentes autónomos y pipelines de procesamiento automático.',
                'features_list': 'Integración con APIs de OpenAI, Anthropic y modelos locales\nProcesamiento inteligente de documentos y PDFs\nScraping ético y pipelines de ingesta de datos\nChatbots contextuales con RAG sobre datos de la empresa',
                'icon': 'bi-cpu',
                'highlight': True,
                'order': 4,
            },
            {
                'title': 'Aplicaciones Móviles Multiplataforma',
                'description': 'Desarrollamos aplicaciones móviles fluidas para iOS y Android con una única base de código, sincronizadas en tiempo real con tu backend.',
                'features_list': 'Experiencia nativa y alto rendimiento\nNotificaciones push y modo offline\nIntegración con cámara, GPS y biometría\nPublicación asistida en Google Play y App Store',
                'icon': 'bi-phone',
                'highlight': False,
                'order': 5,
            },
            {
                'title': 'Consultoría Tecnológica & Sprint 0',
                'description': 'Acompañamiento estratégico antes de escribir código: validación de viabilidad, arquitectura de software, estimación de costos y diseño UX/UI interactivo.',
                'features_list': 'Definición de MVP y roadmap de producto\nAuditoría de seguridad y revisión de código existente\nDiseño de interfaces Figma y flujos de usuario\nSelección del stack tecnológico óptimo',
                'icon': 'bi-lightbulb',
                'highlight': False,
                'order': 6,
            },
        ]
        Service.objects.all().delete()
        for s in services_data:
            Service.objects.create(**s, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(services_data)} servicios creados.'))

        # 3. Technologies
        techs_data = [
            # Backend
            {'name': 'Python', 'category': 'backend', 'icon_class': 'bi-filetype-py', 'color': '#3776ab', 'order': 1},
            {'name': 'Django', 'category': 'backend', 'icon_class': 'bi-hdd-network', 'color': '#092e20', 'order': 2},
            {'name': 'FastAPI', 'category': 'backend', 'icon_class': 'bi-lightning-charge', 'color': '#059669', 'order': 3},
            {'name': 'Node.js', 'category': 'backend', 'icon_class': 'bi-hexagon', 'color': '#339933', 'order': 4},
            
            # Frontend
            {'name': 'JavaScript (ES6+)', 'category': 'frontend', 'icon_class': 'bi-filetype-js', 'color': '#f7df1e', 'order': 5},
            {'name': 'React', 'category': 'frontend', 'icon_class': 'bi-boxes', 'color': '#61dafb', 'order': 6},
            {'name': 'HTML5 & Modern CSS', 'category': 'frontend', 'icon_class': 'bi-filetype-html', 'color': '#e34f26', 'order': 7},
            {'name': 'Bootstrap / Tailwind', 'category': 'frontend', 'icon_class': 'bi-bootstrap', 'color': '#38bdf8', 'order': 8},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'database', 'icon_class': 'bi-database-fill', 'color': '#336791', 'order': 9},
            {'name': 'Redis', 'category': 'database', 'icon_class': 'bi-layers', 'color': '#dc382d', 'order': 10},
            {'name': 'SQLite', 'category': 'database', 'icon_class': 'bi-database', 'color': '#003b57', 'order': 11},

            # Cloud & DevOps
            {'name': 'Docker', 'category': 'cloud', 'icon_class': 'bi-box-seam', 'color': '#2496ed', 'order': 12},
            {'name': 'AWS / Cloud', 'category': 'cloud', 'icon_class': 'bi-cloud', 'color': '#ff9900', 'order': 13},
            {'name': 'CI/CD Pipelines', 'category': 'cloud', 'icon_class': 'bi-arrow-repeat', 'color': '#00ff88', 'order': 14},

            # AI & Automation
            {'name': 'OpenAI / LLMs', 'category': 'ai', 'icon_class': 'bi-cpu-fill', 'color': '#10a37f', 'order': 15},
            {'name': 'Celery Tasks', 'category': 'ai', 'icon_class': 'bi-gear-wide-connected', 'color': '#37814a', 'order': 16},
        ]
        Technology.objects.all().delete()
        for t in techs_data:
            Technology.objects.create(**t, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(techs_data)} tecnologias creadas.'))

        # 4. Process Steps (Metodología)
        steps_data = [
            {
                'step_number': '01',
                'title': 'Discovery & Sprint 0',
                'subtitle': 'Análisis de requerimientos & Arquitectura',
                'description': 'Nos reunimos para entender tu modelo de negocio, usuarios objetivos y alcances. Diseñamos la arquitectura del sistema, el modelo de datos y el roadmap de entregables sin tecnicismos innecesarios.',
                'icon': 'bi-compass',
                'order': 1,
            },
            {
                'step_number': '02',
                'title': 'Diseño UX/UI & Prototipado',
                'subtitle': 'Validación visual antes del código',
                'description': 'Diseñamos wireframes interactivos y la interfaz gráfica completa. Validamos los flujos de navegación contigo para asegurar una experiencia intuitiva, moderna y alineada a tu marca.',
                'icon': 'bi-palette',
                'order': 2,
            },
            {
                'step_number': '03',
                'title': 'Desarrollo Ágil en Sprints',
                'subtitle': 'Entregas funcionales cada 2 semanas',
                'description': 'Escribimos código limpio, tipado y modular en ciclos de sprints quincenales. Tienes acceso a un entorno de staging para probar avances en tiempo real y darnos feedback constante.',
                'icon': 'bi-code-square',
                'order': 3,
            },
            {
                'step_number': '04',
                'title': 'QA, Testing & Seguridad',
                'subtitle': 'Pruebas rigurosas y optimización',
                'description': 'Sometemos el sistema a pruebas de estrés, pruebas unitarias automatizadas y chequeos de seguridad (OWASP). Optimizamos consultas a base de datos y tiempos de respuesta.',
                'icon': 'bi-shield-check',
                'order': 4,
            },
            {
                'step_number': '05',
                'title': 'Despliegue & Soporte 24/7',
                'subtitle': 'Puesta en producción y evolución',
                'description': 'Desplegamos en infraestructura Cloud con pipelines de integración continua (CI/CD), certificados SSL y copias de seguridad automáticas. Brindamos garantía técnica y soporte evolutivo.',
                'icon': 'bi-rocket-takeoff',
                'order': 5,
            },
        ]
        ProcessStep.objects.all().delete()
        for step in steps_data:
            ProcessStep.objects.create(**step, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(steps_data)} pasos de metodologia creados.'))

        # 5. Value Propositions (Garantías)
        value_data = [
            {
                'title': '100% Propiedad del Código',
                'description': 'Todo el código fuente, bases de datos y propiedad intelectual te pertenecen desde la primera línea. Cero ataduras ni licencias ocultas.',
                'icon': 'bi-award-fill',
                'order': 1,
            },
            {
                'title': 'Acuerdo de Confidencialidad (NDA)',
                'description': 'Protegemos tu idea de negocio, estrategia y datos sensibles bajo estricto contrato legal firmado antes de iniciar cualquier fase.',
                'icon': 'bi-shield-lock-fill',
                'order': 2,
            },
            {
                'title': 'Entregas en Tiempo & Presupuesto Cerrado',
                'description': 'Trabajamos con hitos claros y fechas de entrega garantizadas. Sin sorpresas de costos durante el desarrollo del proyecto.',
                'icon': 'bi-calendar-check-fill',
                'order': 3,
            },
            {
                'title': 'Soporte Continuo & Mantenimiento Proactivo',
                'description': 'No te dejamos solo tras el lanzamiento. Monitoreamos el rendimiento, aplicamos actualizaciones de seguridad y escalamos funcionalidades.',
                'icon': 'bi-headset',
                'order': 4,
            },
        ]
        ValueProposition.objects.all().delete()
        for val in value_data:
            ValueProposition.objects.create(**val, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(value_data)} garantias creadas.'))

        # 6. FAQs
        faqs_data = [
            {
                'question': '¿Cómo estiman el costo y plazo de un desarrollo a medida?',
                'answer': 'Analizamos el alcance funcional, la complejidad de integraciones (pasarelas de pago, APIs de terceros, IA), el diseño UX/UI requerido y el tiempo de entrega deseado. Te brindamos una propuesta detallada desglosada por sprints con costo fijo e hitos transparentes.',
                'category': 'payment',
                'order': 1,
            },
            {
                'question': '¿El código fuente y los servidores me pertenecerán?',
                'answer': 'Sí, absolutamente. Al finalizar el proyecto o durante el avance de los sprints, te entregamos acceso total al repositorio en GitHub/GitLab y configuramos la infraestructura en tus propias cuentas de Cloud (AWS, DigitalOcean, etc.).',
                'category': 'tech',
                'order': 2,
            },
            {
                'question': '¿Cómo realizamos el seguimiento del avance durante el proyecto?',
                'answer': 'Utilizamos metodologías ágiles (Scrum). Dispondrás de un canal de comunicación directo (Slack o WhatsApp), reuniones periódicas de revisión al final de cada sprint y acceso a un entorno de prueba (Staging) para validar el software en funcionamiento.',
                'category': 'process',
                'order': 3,
            },
            {
                'question': '¿Qué ocurre si necesito cambios o nuevas funciones en el futuro?',
                'answer': 'Nuestras aplicaciones se construyen con código modular y escalable pensado para evolucionar. Ofrecemos paquetes de horas de mantenimiento mensual o podemos cotizar nuevas fases de desarrollo a medida que tu negocio crezca.',
                'category': 'process',
                'order': 4,
            },
            {
                'question': '¿Pueden integrarse con herramientas y sistemas que ya uso en mi empresa?',
                'answer': 'Sí. Desarrollamos integraciones a medida con ERPs existentes, CRMs (HubSpot, Salesforce), pasarelas de pago (MercadoPago, Stripe, PayPal), sistemas de facturación fiscal electrónica, WhatsApp API y servicios de Google/Microsoft.',
                'category': 'tech',
                'order': 5,
            },
            {
                'question': '¿Cuáles son las modalidades de pago aceptadas?',
                'answer': 'Trabajamos habitualmente con esquema de anticipo inicial (30-40%) y pagos fraccionados contra entrega y validación de cada sprint. Aceptamos transferencias bancarias locales, dólares vía transferencia internacional, Crypto (USDT) y plataformas como Stripe o Wise.',
                'category': 'payment',
                'order': 6,
            },
        ]
        FAQ.objects.all().delete()
        for f in faqs_data:
            FAQ.objects.create(**f, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(faqs_data)} preguntas frecuentes creadas.'))

        # 7. Statistics
        stats_data = [
            {'label': 'Proyectos y Sprints Entregados', 'value': 35, 'suffix': '+', 'icon': 'bi-code-slash', 'order': 1},
            {'label': 'Satisfacción de Clientes', 'value': 99, 'suffix': '%', 'icon': 'bi-star-fill', 'order': 2},
            {'label': 'Disponibilidad de Uptime en Cloud', 'value': 99, 'suffix': '.9%', 'icon': 'bi-cloud-check-fill', 'order': 3},
            {'label': 'Tiempo Máximo de Respuesta', 'value': 24, 'suffix': 'hs', 'icon': 'bi-lightning-fill', 'order': 4},
        ]
        Statistic.objects.all().delete()
        for st in stats_data:
            Statistic.objects.create(**st, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(stats_data)} estadisticas creadas.'))

        # 8. Testimonials
        testimonials_data = [
            {
                'client_name': 'Ignacio Valenzuela',
                'client_position': 'Founder & CEO',
                'client_company': 'LogiTrack SaaS',
                'message': 'Nexus Studio Code desarrolló nuestra plataforma SaaS de logística desde cero. La velocidad de entrega en los sprints y la calidad del código en Django y React nos permitieron levantar nuestra ronda de inversión en tiempo récord.',
                'rating': 5,
                'order': 1,
            },
            {
                'client_name': 'Mariana Dupont',
                'client_position': 'Directora de Operaciones',
                'client_company': 'InnovaHealth',
                'message': 'Necesitábamos digitalizar por completo el sistema de turnos y expedientes médicos. El equipo de Nexus no solo construyó un sistema seguro y rápido, sino que nos asesoró en cada decisión arquitectónica con total transparencia.',
                'rating': 5,
                'order': 2,
            },
            {
                'client_name': 'Carlos Menéndez',
                'client_position': 'CTO',
                'client_company': 'FinPay Latam',
                'message': 'Excelente capacidad técnica para el desarrollo de APIs de alta concurrencia. La integración con pasarelas de pago y la arquitectura en microservicios funcionó impecable desde el primer día de producción.',
                'rating': 5,
                'order': 3,
            },
        ]
        Testimonial.objects.all().delete()
        for tm in testimonials_data:
            Testimonial.objects.create(**tm, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(testimonials_data)} testimonios creados.'))

        # 9. Projects (Portfolio & Case Studies)
        projects_data = [
            {
                'title': 'Plataforma SaaS de Pronósticos Deportivos (Prode Mundial)',
                'slug': 'prode-mundial-saas',
                'category': 'saas',
                'client_name': 'SportsTech Media',
                'short_description': 'Plataforma web de alta concurrencia con sistema de fixtures interactivos, cálculo automático de puntos, tablas de posiciones en tiempo real y pagos.',
                'description': 'Desarrollo integral de una plataforma web para torneos y pronósticos deportivos en vivo. Diseñada para soportar picos masivos de tráfico concurrente durante eventos de fútbol internacional con latencia ultrabaja.',
                'challenge': 'El cliente requería una plataforma interactiva capaz de soportar más de 15.000 usuarios concurrentes enviando pronósticos simultáneamente antes de cada partido, con sincronización de resultados en tiempo real y pasarela de suscripciones.',
                'solution': 'Diseñamos una arquitectura basada en Django + PostgreSQL con capa de caché en Redis para consultas calientes. Implementamos tareas en segundo plano con Celery para el recálculo masivo de posiciones y una UI dinámica en JavaScript vanilla ultra liviana.',
                'results': '✓ +25.000 usuarios registrados activos\n✓ Tiempo medio de respuesta < 95ms\n✓ 0 caídas durante picos de eventos masivos\n✓ Integración automatizada con MercadoPago y Stripe',
                'technologies': 'Python, Django, PostgreSQL, Redis, Celery, Docker, JavaScript, CSS3',
                'status': 'completed',
                'is_featured': True,
                'order': 1,
                'completion_date': '2025',
                'public_url': 'https://nexusstudiocode.com',
                'github_url': '',
            },
            {
                'title': 'Sistema de Gestión Integral para Complejos Deportivos',
                'slug': 'complejo-deportivo-erp',
                'category': 'erp',
                'client_name': 'Red de Clubes Deportivos',
                'short_description': 'Sistema ERP personalizado para gestión de turnos de canchas, facturación electrónica, control de caja diaria y membresías de socios.',
                'description': 'Solución integral que reemplazó planillas manuales de Excel por una plataforma centralizada y accesible desde móviles y computadoras para el personal administrativo y los clientes del complejo.',
                'challenge': 'Pérdida constante de turnos por cancelaciones tardías, falta de visibilidad en los cobros de seña y dificultad para cuadrar cajas entre múltiples sedes físicas.',
                'solution': 'Construcción de un ERP multi-sede con calendario interactivo tipo drag-and-drop, pasarela de cobro de señas automáticas por link de WhatsApp, control de inventario de bar/tienda y liquidación de sueldos.',
                'results': '✓ 45% de aumento en la ocupación de canchas\n✓ Reducción del 90% en no-shows gracias a señas automáticas\n✓ Cuadre de caja automatizado y exportación contable en 1 clic',
                'technologies': 'Python, Django, PostgreSQL, Tailwind CSS, JavaScript, WhatsApp API',
                'status': 'completed',
                'is_featured': True,
                'order': 2,
                'completion_date': '2024',
                'public_url': '',
                'github_url': '',
            },
            {
                'title': 'Motor de APIs & Microservicio de Facturación Electrónica',
                'slug': 'api-facturacion-electronica',
                'category': 'api',
                'client_name': 'Fintech B2B Solutions',
                'short_description': 'API RESTful de alta velocidad para emisión y validación de comprobantes fiscales electrónicos en lote con autenticación OAuth2.',
                'description': 'Microservicio backend para procesamiento seguro de comprobantes fiscales, generación de PDFs con código QR y sincronización asíncrona con organismos tributarios.',
                'challenge': 'La empresa necesitaba un backend desacoplado que pudiera ser consumido por 4 aplicaciones distintas simultáneamente, garantizando idempotencia en cada transacción fiscal.',
                'solution': 'Desarrollamos una API REST documentada en Swagger/OpenAPI con rate limiting, firmas criptográficas y reintentos automáticos ante fallas de conectividad externa.',
                'results': '✓ Más de 120.000 facturas emitidas por mes\n✓ Tiempo de emisión reducido de 4.2s a 0.35s\n✓ Cobertura de tests automatizados del 94%',
                'technologies': 'Python, FastAPI, Django REST, PostgreSQL, Docker, AWS S3, PyTest',
                'status': 'completed',
                'is_featured': True,
                'order': 3,
                'completion_date': '2025',
                'public_url': '',
                'github_url': '',
            },
            {
                'title': 'Portal de E-commerce B2B con Cotizador y Catálogo Privado',
                'slug': 'ecommerce-b2b-distribuidora',
                'category': 'web',
                'client_name': 'Distribuidora Mayorista Industrial',
                'short_description': 'Portal mayorista con listas de precios segmentadas por tipo de cliente, cotizaciones en PDF dinámicas y pedidos con cuenta corriente.',
                'description': 'Plataforma B2B que transformó el canal de ventas tradicional en un sistema digital disponible 24/7 para distribuidores y clientes corporativos.',
                'challenge': 'El proceso de cotización manual por correo demoraba hasta 48 horas y los vendedores cometían errores con listas de precios desactualizadas.',
                'solution': 'Portal web autogestionable con autenticación empresarial, cálculo automático de descuentos por volumen, generación de órdenes de compra y panel de stock en tiempo real.',
                'results': '✓ Tiempos de cotización reducidos de 48h a 3 minutos\n✓ Incremento del 32% en ventas en el primer trimestre\n✓ 100% de reducción en errores de precios',
                'technologies': 'Django, PostgreSQL, React, Bootstrap 5, Redis, WeasyPrint',
                'status': 'completed',
                'is_featured': True,
                'order': 4,
                'completion_date': '2024',
                'public_url': '',
                'github_url': '',
            },
        ]
        Project.objects.all().delete()
        for p in projects_data:
            Project.objects.create(**p, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(projects_data)} proyectos y casos de estudio creados.'))

        # 10. Social Links
        socials_data = [
            {'platform': 'github', 'url': 'https://github.com', 'order': 1},
            {'platform': 'linkedin', 'url': 'https://linkedin.com', 'order': 2},
            {'platform': 'whatsapp', 'url': 'https://wa.me/5491155550199', 'order': 3},
            {'platform': 'instagram', 'url': 'https://instagram.com', 'order': 4},
        ]
        SocialLink.objects.all().delete()
        for soc in socials_data:
            SocialLink.objects.create(**soc, is_active=True)
        self.stdout.write(self.style.SUCCESS(f'[OK] {len(socials_data)} redes sociales creadas.'))

        self.stdout.write(self.style.SUCCESS('\n[OK] Sembrado completado exitosamente. Todo el contenido corporativo esta listo en la base de datos!'))
