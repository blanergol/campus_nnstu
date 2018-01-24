from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^student_council', views.student_council, name='student_council'),
    url(r'^leadership', views.leadership, name='leadership'),
    url(r'^dormitories', views.dormitories, name='dormitories'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^newspaper', views.newspaper, name='newspaper'),
    url(r'^student_unification', views.student_unification, name='student_unification'),
]
