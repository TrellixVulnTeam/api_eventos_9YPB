import requests
from django.shortcuts import render, redirect
# from eventos import AccessToken
from usuario.forms import UsuarioLoginForm
from constant.constant import URLBASE


def listar_eventos(request):
    # url = 'https://apieventos.conveniar.com.br/conveniar/api/eventos?pagina=1&limite=50'
    url = URLBASE + '?pagina=1&limite=50'

    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
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
    else:
        return render(request, 'eventos/error404.html')


def eventos_dados(request, cod_evento):
    codigo_evento = cod_evento
    url = URLBASE + 'ids?codEventos=' + codigo_evento
    print(url)
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()[0]

        eventos_data = []

        if data['Informacoes'] is not None:
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
        else:
            evento = {
                'CodEvento': data['CodEvento'],
                'NomeEvento': data['NomeEvento'],
                'NomeConvenio': data['NomeConvenio'],
                'Categoria': data['Categoria'],
                'Situacao': data['Situacao'],
                'DataInicio': data['DataInicio'].strftime("%Y-%m-%d %H:%M:%S"),
                'DataFim': data['DataFim'].strftime("%Y-%m-%d %H:%M:%S"),
                'NumeroVagas': data['NumeroVagas'],
                # 'DescricaoEventoInformacao': data['Informacoes']['DescricaoEventoInformacao']
            }
            eventos_data.append(evento)

        form = UsuarioLoginForm()

        context = {
            'eventos_data': eventos_data,
            'form': form
        }

        return render(request, 'eventos/dados-do-curso.html', context)

    else:
        return render(request, 'eventos/error404.html')
