from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'answer/(?P<pk>[0-9]+)/$', views.answer_full, name='answer_full'),
    url(r'^new_issue', views.new_issue, name='new_issue'),
    url(r'^issues', views.issues, name='issues'),
    url(r'^answer', views.answer, name='answer'),
    url(r'^search', views.search, name='search'),
]
