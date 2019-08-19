import requests
from django.shortcuts import render, redirect
# from eventos import AccessToken
from usuario.forms import UsuarioLoginForm
from constant.constant import URLBASE
import datetime


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
                'codEvento': data['CodEvento'],
                'nomeEvento': data['NomeEvento'],
                'nomeConvenio': data['NomeConvenio'],
                'categoria': data['Categoria'],
                'situacao': data['Situacao'],
                'dataInicio': data['DataInicio'],
                'dataFim': data['DataFim'],
                'numeroVagas': data['NumeroVagas']
            }
            eventos_data.append(eventos)

        context = {
            'eventos_data': eventos_data,
            'form': form
        }

        return render(request, 'eventos/index.html', context)
    else:
        return render(request, 'eventos/error404.html')


def formatar_data(datas):
    nova_data = (datas[8:10] + "/" + datas[5:7] + "/" + datas[0:4])
    return nova_data


def data_atual():
    hoje = datetime.datetime.now().date()
    return formatar_data(str(hoje))


def eventos_dados(request, cod_evento):
    codigo_evento = cod_evento
    url = URLBASE + 'ids?codEventos=' + codigo_evento
    headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()[0]

        eventos_data = []

        if data['Informacoes'] is not None:
            nova_data_inicio = formatar_data(data['DataInicio'])
            nova_data_fim = formatar_data(data['DataFim'])

            evento = {
                    'CodEvento': data['CodEvento'],
                    'NomeEvento': data['NomeEvento'],
                    'NomeConvenio': data['NomeConvenio'],
                    'Categoria': data['Categoria'],
                    'Situacao': data['Situacao'],
                    'DataInicio': nova_data_inicio,
                    'DataFim': nova_data_fim,
                    'NumeroVagas': data['NumeroVagas'],
                    'DescricaoEventoInformacao': data['Informacoes']['DescricaoEventoInformacao']
            }
            eventos_data.append(evento)
        else:
            nova_data_inicio = formatar_data(data['DataInicio'])
            nova_data_fim = formatar_data(data['DataFim'])

            evento = {
                'CodEvento': data['CodEvento'],
                'NomeEvento': data['NomeEvento'],
                'NomeConvenio': data['NomeConvenio'],
                'Categoria': data['Categoria'],
                'Situacao': data['Situacao'],
                'DataInicio': nova_data_fim,
                'DataFim': nova_data_inicio,
                'NumeroVagas': data['NumeroVagas'],
            }
            eventos_data.append(evento)

        form = UsuarioLoginForm()

        hoje = data_atual()

        context = {
            'eventos_data': eventos_data,
            'form': form,
            'hoje': hoje
        }

        return render(request, 'eventos/dados-do-curso.html', context)

    else:
        return render(request, 'eventos/error404.html')
