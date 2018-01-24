from django.contrib import admin
from .models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location', 'date', 'time_start', 'time_end']
    list_filter = ['date']
    search_fields = ['title', 'text']


admin.site.register(Events, EventsAdmin)
