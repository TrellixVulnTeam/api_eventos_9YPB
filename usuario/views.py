from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from usuario.models import Usuario
from .forms import UsuarioLoginForm
from constant.constant import URLBASE, KEY
import requests


def login(request):
    url = URLBASE + 'oauth/token'

    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            registro = form.cleaned_data['registro']
            senha = form.cleaned_data['senha']

            usuario = get_object_or_404(Usuario, registro=registro)

            if usuario.registro == registro and senha == usuario.senha:
                header = {
                             'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'
                          }
                r = requests.get(url, auth=(registro, senha), headers=header)

                if r.status_code == 200:
                    usuario.token = r.json()['AccessToken']
                    usuario.save()

                q = Usuario.objects.filter(registro=usuario.registro)
                if q:
                    return redirect('dashboard', usuario.registro)
            else:
                # ERROR = 40
                # messages.add_message(request, ERROR, 'A serious error occurred.')
                return redirect('listar_eventos')

    return redirect('listar_eventos')


def dashboard(request, registro):
    # Dados do usuario

    url = URLBASE + 'usuario/'
    usuario = Usuario.objects.get(registro=registro)

    header = {
        'Authorization': usuario.token,
        'X-API-KEY': KEY
    }
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        data = r.json()
        usuario_data = []

        usuario = {
            'Nome': data['Nome'],
            'registro': data['NumRegistro']
        }

        usuario_data.append(usuario)

        # Dados do eventos
        url = URLBASE + 'inscricoes?pagina=1&limite=50'
        usuario = Usuario.objects.get(registro=registro)

        header = {
            'Authorization': usuario.token,
            'X-API-KEY': KEY
        }

        r = requests.get(url, headers=header)

        evento_data = []

        for i in range(len(r.json())):
            data = r.json()[i]

            if data['NomeStatus'] == 'Inscrito':
                evento = {
                    'codEvento': data['CodEvento'],
                    'nomeEvento': data['NomeEvento'],
                    'nomeCategoria_inscricao': data['NomeCategoriaInscricao'],
                    'nomeStatus': data['NomeStatus'],
                    'registro': data['NumeroInscricao'],
                    'codEventoInscricao': data['CodEventoInscricao']
                }

                evento_data.append(evento)

        context = {
            'usuario_data': usuario_data,
            'evento_data': evento_data
        }

        print(evento_data)
        print(usuario_data)

        return render(request, 'usuario/dashboard.html', context)
    else:
        return render(request, 'eventos/error404.html')


def eventos_cursos(request, registro):

    url = URLBASE + 'inscricoes?pagina=1&limite=50'
    usuario = Usuario.objects.get(registro=registro)

    header = {
        'Authorization': usuario.token
    }

    r = requests.get(url, headers=header)
    evento_data = []

    for i in range(len(r.json())):
        data = r.json()[i]
        evento = {
            'codEvento': data['CodEvento'],
            'CodEventoInscricao': data['CodEventoInscricao'],
            'nomeEvento': data['NomeEvento'],
            'nomeCategoria_inscricao': data['NomeCategoriaInscricao'],
            'nomeStatus': data['NomeStatus'],
            'registro': data['NumeroInscricao'],
        }

        evento_data.append(evento)

    url_usuario = "https://apieventos.conveniar.com.br/conveniar/api/eventos/usuario"

    r = requests.get(url_usuario, headers=header)
    data = r.json()
    usuario_data = []

    usuario = {
        'registro': data['NumRegistro'],
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
        'usuario_data': usuario_data,
        'evento_data': evento_data
    }

    return render(request, 'usuario/lista-curso-inscrito.html', context)


def listar_documento_financeiro(request, registro, codeventoinscricao):
    url = URLBASE + "inscricao/"+(str(codeventoinscricao))+"/documentos?pagina=1&limite=50"
    usuario = Usuario.objects.get(registro=registro)

    header = {
        'Authorization': usuario.token,
        'X-API-KEY': KEY
    }

    r = requests.get(url, headers=header)

    documentos_financieros = []

    for i in range(len(r.json())):
        data = r.json()[i]
        documentos = {
            'CodDocumento': data['CodDocumento'],
            'Parcela': data['Parcela'],
            'CodEvento': data['CodEvento'],
            'TipoDocumento': data['TipoDocumento'],
            'DataPagamento': data['DataPagamento'],
            'Valor': data['Valor'],
            'ValorPago': data['ValorPago'],
            'NomeTipoPagamento': data['NomeTipoPagamento'],
            'NomeStatus': data['NomeStatus'],
        }

        documentos_financieros.append(documentos)

    url_usuario = URLBASE + '/usuario'

    r = requests.get(url_usuario, headers=header)
    data = r.json()
    usuario_data = []

    usuario = {
        'registro': data['NumRegistro'],
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
        'usuario_data': usuario_data,
        'documentos_financieros': documentos_financieros
    }

    return render(request, 'usuario/dashboard.html', context)


def dados_usuario(request, registro):
    url = URLBASE + 'usuario/'

    usuario = Usuario.objects.get(registro=registro)

    header = {
        'Authorization': usuario.token,
        'X-API-KEY': KEY
    }

    r = requests.get(url, headers=header)

    data = r.json()
    usuario_data = []

    usuario = {
        'registro': data['NumRegistro'],
        'Nome': data['Nome'],
        'Cracha': data['Cracha'],
        'Email': data['Email'],
        'Documento': data['Documento'],
        'TelefoneCelular': data['TelefoneCelular'],
        'TelefoneCasa': data['TelefoneCasa'],
        'TelefoneEmpresa': data['TelefoneEmpresa'],
        'CEP': data['CEP'],
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


# def exibir_tela_cadatrar_inscrito(request):return render(request, 'usuario/registrar.html')


def salvar_dados(request):
    if request.method == 'POST':
        # Dados Pessoais
        request.POST.get('nome_completo')
        request.POST.get('cracha')
        request.POST.get('cpf')
        request.POST.get('email')
        request.POST.get('senha')
        # request.POST.get('nome_completo')


# def cadastrar_inscrito(request):
#     if request.method == 'POST':
#         print('informação enviada')
#     return 0
