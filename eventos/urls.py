from django.urls import path
from . import views

urlpatterns = [
    path('', views.token, name='listar_eventos'),
]
