from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # Usuario
    url(r'^auth/login$', views.login, name='auth_login'),
    url(r'^dashboard/(?P<registro>[\d]+)$', views.dashboard, name='dashboard'),
    url(r'^dados-usuario/(?P<registro>[\d]+)$', views.dados_usuario, name='dados_usuario'),
]
