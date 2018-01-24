from django.contrib import admin
from .models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'middle_name', 'email', 'phone', 'institute', 'group', 'dormitory', 'room']
    list_filter = ['institute', 'group', 'dormitory', 'room']
    search_fields = ['surname', 'name', 'middle_name', 'institute', 'group', 'dormitory', 'room']


admin.site.register(Students, StudentsAdmin)
