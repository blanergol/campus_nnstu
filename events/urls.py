from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'events/(?P<pk>[0-9]+)/$', views.full, name='full'),
    url(r'events', views.main, name='main'),
]
