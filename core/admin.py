from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteConfig, Service, Technology, ProcessStep,
    ValueProposition, FAQ, Statistic, Testimonial,
    SocialLink, QuoteRequest
)


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información General', {'fields': ('company_name', 'tagline', 'logo', 'favicon', 'experience_years')}),
        ('Hero Section', {'fields': ('hero_badge_text', 'hero_title', 'hero_subtitle')}),
        ('Sobre Nosotros', {'fields': ('about_history', 'about_mission', 'about_vision', 'about_values')}),
        ('Contacto & WhatsApp', {
            'fields': ('email', 'phone', 'whatsapp_number', 'whatsapp_message', 'meeting_url', 'address'),
            'description': 'Aquí puedes configurar el número de WhatsApp para el botón flotante, los formularios y los enlaces directos de toda la web.'
        }),
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
    search_fields = ('title', 'description', 'features_list')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color_preview', 'order', 'is_active')
    list_editable = ('category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)

    def color_preview(self, obj):
        return format_html(
            '<span style="background:{};width:20px;height:20px;display:inline-block;border-radius:3px;vertical-align:middle;margin-right:6px;"></span> {}',
            obj.color, obj.color
        )
    color_preview.short_description = 'Color'


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('step_number', 'title', 'subtitle', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(ValueProposition)
class ValuePropositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order', 'is_active')
    list_editable = ('category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'suffix', 'icon', 'order', 'is_active')
    list_editable = ('value', 'suffix', 'order', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'rating')
    search_fields = ('client_name', 'client_company', 'message')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'project_type', 'estimated_cost_display', 'status', 'created_at')
    list_filter = ('status', 'project_type', 'created_at')
    search_fields = ('name', 'email', 'phone', 'company', 'description')
    list_editable = ('status',)
    readonly_fields = ('name', 'email', 'phone', 'company', 'project_type', 'features', 'budget_range', 'timeline', 'description', 'estimated_cost_display', 'ip_address', 'created_at')
    date_hierarchy = 'created_at'

