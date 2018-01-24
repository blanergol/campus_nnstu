from django.contrib import admin
from .models import DormitoriesImg, Dormitories


class DormitoriesImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class DormitoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(DormitoriesImg, DormitoriesImgAdmin)
admin.site.register(Dormitories, DormitoriesAdmin)
