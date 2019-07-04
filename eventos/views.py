import requests
from django.shortcuts import render, redirect
# from eventos import AccessToken
from usuario.forms import UsuarioLoginForm


def listar_eventos(request):
    url = 'https://apieventos.conveniar.com.br/conveniar/api/eventos?pagina=1&limite=50'
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)
    eventos_data = []

    form = UsuarioLoginForm()

    for item in range(len(r.json())):
        data = r.json()[item]
        eventos = {
            'CodEvento': data['CodEvento'],
            'NomeEvento': data['NomeEvento'],
            'NomeConvenio': data['NomeConvenio'],
            'Categoria': data['Categoria'],
            'Situacao': data['Situacao'],
            'DataInicio': data['DataInicio'],
            'DataFim': data['DataFim'],
            'NumeroVagas': data['NumeroVagas']
        }
        eventos_data.append(eventos)

    context = {
        'eventos_data': eventos_data,
        'form': form
    }

    return render(request, 'eventos/index.html', context)


def eventos_dados(request, cod_evento):
    codigo_evento = cod_evento
    url = 'https://apieventos.conveniar.com.br/conveniar/api/eventos/ids?codEventos=' + codigo_evento
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)
    data = r.json()[0]

    eventos_data = []

    evento = {
            'CodEvento': data['CodEvento'],
            'NomeEvento': data['NomeEvento'],
            'NomeConvenio': data['NomeConvenio'],
            'Categoria': data['Categoria'],
            'Situacao': data['Situacao'],
            'DataInicio': data['DataInicio'],
            'DataFim': data['DataFim'],
            'NumeroVagas': data['NumeroVagas'],
            'DescricaoEventoInformacao': data['Informacoes']['DescricaoEventoInformacao']
    }

    eventos_data.append(evento)

    context = {
        'eventos_data': eventos_data
    }

    return render(request, 'eventos/dados-do-curso.html', context)
