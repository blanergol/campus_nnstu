from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dormitories', views.main, name='main'),
]
