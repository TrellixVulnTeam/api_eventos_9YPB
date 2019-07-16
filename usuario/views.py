from django.shortcuts import render, redirect
import requests

from usuario.models import Usuario
from .forms import UsuarioLoginForm


def login(request):
    url = "https://apiauth.conveniar.com.br/conveniar/api/eventos/oauth/token"

    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            usuario = Usuario()
            usuario.registro = form.cleaned_data['registro']
            usuario.senha = form.cleaned_data['senha']

            header = {
                        'X-API-KEY': '7e61b6bb-6841-415f-954e-5e2ba445cc7c'
                     }
            r = requests.get(url, auth=(usuario.registro, usuario.senha), headers=header)

            if r.status_code == 200:
                usuario.token = r.json()['AccessToken']

                # __REGRISTRO = usuario.registro
                # __SENHA = usuario.senha
                # __TOKEN = usuario.token

                usuario.save()

                return redirect('dashboard', usuario.registro)

    return redirect('listar_eventos')


def dashboard(request, registro):

    usuario = Usuario.objects.filter(registro=registro)
    print(usuario)

    return render(request, 'usuario/dashboard.html')


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
