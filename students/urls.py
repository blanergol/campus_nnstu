from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'students/(?P<pk>[0-9]+)/$', views.main, name='main'),
    url(r'students/auth', views.auth, name='auth'),
    url(r'students/reg', views.reg, name='reg'),
    url(r'auth_students', views.auth_students, name='auth_students'),
    url(r'reg_mp_students', views.reg_mp_students, name='reg_mp_students'),
    url(r'reg_students', views.reg_students, name='reg_students'),
    url(r'students/logout', views.logout_students, name='logout_students'),
]
