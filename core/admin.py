from django.contrib import admin
from django.utils.html import format_html
from .models import SiteConfig, Service, Technology, Statistic, Testimonial, SocialLink


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información General', {'fields': ('company_name', 'tagline', 'logo', 'favicon')}),
        ('Hero Section', {'fields': ('hero_title', 'hero_subtitle')}),
        ('Sobre Nosotros', {'fields': ('about_history', 'about_mission', 'about_vision', 'about_values')}),
        ('Contacto', {'fields': ('email', 'phone', 'address')}),
        ('SEO', {'fields': ('meta_description', 'meta_keywords', 'google_analytics')}),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'highlight', 'is_active')
    list_editable = ('order', 'highlight', 'is_active')
    list_filter = ('is_active', 'highlight')
    search_fields = ('title', 'description')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')

    def color_preview(self, obj):
        return format_html(
            '<span style="background:{};width:20px;height:20px;display:inline-block;border-radius:3px;"></span> {}',
            obj.color, obj.color
        )
    color_preview.short_description = 'Color'


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'suffix', 'icon', 'order', 'is_active')
    list_editable = ('value', 'order', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'rating')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
