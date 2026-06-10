from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.filter(is_active=True)
    return render(request, 'portfolio/list.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related = Project.objects.filter(is_active=True).exclude(pk=project.pk)[:3]
    return render(request, 'portfolio/detail.html', {'project': project, 'related': related})
