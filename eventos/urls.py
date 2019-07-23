from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.listar_eventos, name='listar_eventos'),
    url(r'^portal-eventos/$', views.listar_eventos, name='listar_eventos'),
    url('eventos/(?P<cod_evento>[\d]+)$', views.eventos_dados, name='eventos_dados'),
]
