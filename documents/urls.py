from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'documents', views.main, name='main'),
]
