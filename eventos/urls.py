from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # url('', views.token, name='token'),
    url(r'^portal-eventos/$', views.listar_eventos, name='listar_eventos'),
    url('eventos/(?P<cod_evento>[\d]+)$', views.eventos_dados, name='eventos_dados'),

    # Usuario
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dados-usuario/$', views.dados_usuario, name='dados_usuario'),
]
