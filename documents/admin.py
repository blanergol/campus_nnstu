from django.contrib import admin
from .models import Documents


class DocuemntsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Documents, DocuemntsAdmin)
