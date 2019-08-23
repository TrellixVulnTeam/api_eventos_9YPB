from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # Usuario
    url(r'^auth/login$', views.login, name='auth_login'),
    url(r'^dashboard/(?P<registro>[\d]+)$', views.dashboard, name='dashboard'),
    url(r'^dados-usuario/(?P<registro>[\d]+)$', views.dados_usuario, name='dados_usuario'),
    url(r'^salvar-dados-usuario/(?P<registro>[\d]+)$', views.salvar_dados, name='salvar_dados'),

    # url(r'^alterar/dados/(?P<registro>[\d]+)$', views.alterar_cadastro_inscrito, name='alterar_cadastro_inscrito'),
    url(r'^cadastro/inscrito/$', views.exibir_tela_cadatrar_inscrito, name='cadastro_inscrito'),


    url(r'^eventos/cursos/inscrito/(?P<registro>[\d]+)$', views.eventos_cursos, name='eventos_cursos'),
    url(r'^eventos/cursos/documento/financeiro/(?P<registro>[\d]+)/(?P<codeventoinscricao>[\d]+)$',
        views.listar_documento_financeiro, name='listar_documento_financeiro'),
]
