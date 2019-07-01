from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.token, name='token'),
    url('portal-eventos/$', views.listar_eventos, name='listar_eventos'),
    url('evento/(?P<cod_evento>[\d]+)$', views.dados_eventos, name='dados_eventos'),
]
