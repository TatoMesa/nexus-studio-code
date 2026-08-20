from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'status', 'image_preview', 'is_featured', 'order', 'is_active')
    list_editable = ('category', 'status', 'is_featured', 'order', 'is_active')
    list_filter = ('category', 'status', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'technologies', 'client_name', 'challenge', 'solution')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Información General', {'fields': ('title', 'slug', 'category', 'client_name', 'completion_date', 'short_description', 'description')}),
        ('Imagen', {'fields': ('image', 'image_preview')}),
        ('Caso de Estudio (Impacto & Métricas)', {
            'fields': ('challenge', 'solution', 'results'),
            'description': 'Información estructurada para presentar el proyecto a clientes corporativos.'
        }),
        ('Stack Técnico & Enlaces', {'fields': ('technologies', 'status', 'public_url', 'github_url')}),
        ('Visibilidad & Destacado', {'fields': ('is_featured', 'is_active', 'order')}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;border-radius:4px;object-fit:cover;" />', obj.image.url)
        return '—'
    image_preview.short_description = 'Vista previa'

