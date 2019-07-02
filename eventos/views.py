import requests
from django.shortcuts import render, redirect


# def token(request):
#     url = 'https://apiauth.conveniar.com.br/conveniar/api/eventos/oauth/token'
#     headers = {'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'}
#     r = requests.get(url, auth=('155', 'goto'), headers=headers)
#
#     return redirect('listar_eventos')

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


def dashboard(request):

    return render(request, 'usuario/dashboard.html')


def dados_usuario(request):
    url = "https://apieventos.conveniar.com.br/conveniar/api/eventos/cadastro/usuario/pessoa"
    r = requests.get(url,
                     headers={
                         'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNTUiLCJqdGkiOiJmNTFlYzgxOC05ZTZkLTRmNTAtYjBjNi02NDM4ZmRhOTgzYWUiLCJjbGllbnRBcHAiOiI5YmEzMmRiZi1mNzU1LTQ2MjQtYWM1OC01MjRlYmE3Y2U0YTkiLCJJZGVudGlmaWVyVHlwZSI6IlBvcnRhbEV2ZW50b3NBcGkiLCJyb2xlIjoiRXZlbnRvcyIsInNlcnZlciI6IkludGVybm8iLCJhdXRob3JpemVkQWNjZXNzR3JvdXAiOiI3NTY3YzUyMC0yNTA1LTRmMmMtYTdiYy1lZTVjZWU3ZDE1YzciLCJpZGVudGlmaWVyIjoiMTU1IiwiZXhwIjoxNTYyMTAzMjc3LCJpc3MiOiJodHRwczovL2FwaWF1dGguY29udmVuaWFyLmNvbS5iciIsImF1ZCI6IlBvcnRhbEV2ZW50b3NBcGkifQ.7JNsrVg5lXqEK0HpTWdpDEPdIeUpzRefShGtcueCmZc'
                     })
    data = r.json()
    usuario_data = []

    usuario = {
        'CodPessoaEvento': data['CodPessoaEvento'],
        'NumRegistro': data['NumRegistro'],
        'Nome': data['Nome'],
        'Cracha': data['Cracha'],
        'Email': data['Email'],
        'TelefoneCelular': data['TelefoneCelular'],
        'TelefoneCasa': data['TelefoneCasa'],
        'TelefoneEmpresa': data['TelefoneEmpresa'],
        'Endereco': data['Endereco'],
        'Bairro': data['Bairro'],
        'Cidade': data['Cidade'],
        'Estado': data['Estado'],
        'Pais': data['Pais'],
    }
    usuario_data.append(usuario)

    context = {
        'usuario_data': usuario_data
    }

    return render(request, 'usuario/dados-pessoais.html', context)
