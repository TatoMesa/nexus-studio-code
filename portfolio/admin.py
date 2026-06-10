from django.contrib import admin
from django.utils.html import format_html
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'image_preview', 'is_featured', 'order', 'is_active')
    list_editable = ('status', 'is_featured', 'order', 'is_active')
    list_filter = ('status', 'is_featured', 'is_active')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Información del Proyecto', {'fields': ('title', 'slug', 'description', 'short_description')}),
        ('Imagen', {'fields': ('image', 'image_preview')}),
        ('Detalles Técnicos', {'fields': ('technologies', 'status')}),
        ('URLs', {'fields': ('public_url', 'github_url')}),
        ('Visibilidad', {'fields': ('is_featured', 'is_active', 'order')}),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:80px;border-radius:4px;" />', obj.image.url)
        return '—'
    image_preview.short_description = 'Vista previa'
