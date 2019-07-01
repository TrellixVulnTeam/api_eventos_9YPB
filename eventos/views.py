import requests
from django.shortcuts import render, redirect


def token(request):
    url = 'https://apiauth.conveniar.com.br/conveniar/api/eventos/oauth/token'
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, auth=('155', 'goto'), headers=headers)

    return render(request, 'eventos/listar_eventos.html')


def listar_eventos(request):
    url = 'https://apieventos.conveniar.com.br/conveniar/api/eventos?pagina=1&limite=50'
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)
    eventos_data = []

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
        'eventos_data': eventos_data
    }

    return render(request, 'eventos/index.html', context)


def dados_eventos(request, cod_eventos):

    return render(request, 'eventos/dados-do-curso.html')
