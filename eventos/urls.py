from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('portal-eventos$', views.listar_eventos, name='listar_eventos'),
    url('', views.token, name='token'),

]
