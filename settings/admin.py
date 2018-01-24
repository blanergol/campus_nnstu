from django.contrib import admin
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Настройки для поисковых систем', {
            'fields': ('title', 'description')
        }),
        ('Контактые данные на всех страницах', {
            'fields': ('phone', 'address')
        }),
        ('Социальные сети', {
            'fields': ('link_instagram', 'link_vk', 'link_youtube')
        }),
        ('Виртуальная приемная', {
            'fields': ['rules_vr']
        }),
        ('Другие настройки', {
            'fields': ('description_short_about', 'count_articles', 'count_events', 'description_newspaper', 'description_student_council_dormitories')
        }),
        ('Модули портала', {
            'fields': ('enable_vr', 'enable_students')
        }),
    )

    list_display = ['id', 'title', 'description', 'count_articles', 'count_events', 'enable_vr', 'enable_students']
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Settings, SettingsAdmin)
