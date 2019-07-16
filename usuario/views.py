from django.shortcuts import render, redirect, get_object_or_404
import requests

from usuario.models import Usuario
from .forms import UsuarioLoginForm


def login(request):
    url = "https://apiauth.conveniar.com.br/conveniar/api/eventos/oauth/token"

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
                return redirect('listar_eventos')

    return redirect('listar_eventos')


def dashboard(request, registro):

    url = 'https://apieventos.conveniar.com.br/conveniar/api/eventos/usuario'
    usuario = Usuario.objects.get(registro=registro)

    header = {
        'Authorization': usuario.token
    }

    r = requests.get(url, headers=header)

    data = r.json()
    usuario_data = []

    usuario = {
        'Nome': data['Nome']
    }

    usuario_data.append(usuario)

    context = {
        'usuario_data': usuario_data
    }

    return render(request, 'usuario/dashboard.html', context)


def dados_usuario(request):
    url = "https://apieventos.conveniar.com.br/conveniar/api/eventos/cadastro/usuario/pessoa"
    r = requests.get(url,
                     headers={
                         'Authorization':'AccessToken'
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
