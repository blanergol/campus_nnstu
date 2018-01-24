from django.contrib import admin
from .models import Issues


class IssuesAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']
    search_fields = ['question', 'answer', 'subject', 'who_sub']
    list_filter = ['employees', 'who', 'publication']

admin.site.register(Issues, IssuesAdmin)
