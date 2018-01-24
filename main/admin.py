from django.contrib import admin
from .models import Slider, Employees, Contact, StudentCouncil, Leadership, Newspaper


class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'button_text', 'button_link', 'img']


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'post', 'description', 'email', 'phone', 'photo', 'show_main_page_status', 'student_unification_status']
    search_fields = ['name', 'description']


class LeadershipAdmin(admin.ModelAdmin):
    list_display = ['id']


class StudentCouncilAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'description']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'email_form', 'address', 'phone', 'email', 'contact_leadership', 'contact_ssg']
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Newspaper, NewspaperAdmin)
admin.site.register(Leadership, LeadershipAdmin)
admin.site.register(StudentCouncil, StudentCouncilAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Contact, ContactAdmin)
