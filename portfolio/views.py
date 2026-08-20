from django.shortcuts import render, get_object_or_404
from .models import Project
from core.models import SiteConfig


def project_list(request):
    config = SiteConfig.get_config()
    selected_category = request.GET.get('categoria', 'all')
    projects_qs = Project.objects.filter(is_active=True)
    
    if selected_category and selected_category != 'all':
        projects = projects_qs.filter(category=selected_category)
    else:
        projects = projects_qs

    categories = [
        ('all', 'Todos los Proyectos'),
        ('saas', 'Plataformas SaaS'),
        ('erp', 'Sistemas ERP / Gestión'),
        ('api', 'APIs & Backend'),
        ('web', 'Web Apps & E-commerce'),
        ('mobile', 'Apps Móviles'),
    ]

    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
        'total_count': projects_qs.count(),
        'config': config,
        'page_title': f'Portafolio y Casos de Éxito — {config.company_name}',
    }
    return render(request, 'portfolio/list.html', context)


def project_detail(request, slug):
    config = SiteConfig.get_config()
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related = Project.objects.filter(is_active=True).exclude(pk=project.pk).filter(category=project.category)[:3]
    if not related.exists():
        related = Project.objects.filter(is_active=True).exclude(pk=project.pk)[:3]

    context = {
        'project': project,
        'related': related,
        'config': config,
        'page_title': f'{project.title} — Caso de Estudio | {config.company_name}',
    }
    return render(request, 'portfolio/detail.html', context)

