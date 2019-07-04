from django.shortcuts import render, redirect
import requests

from usuario.models import Usuario
from .forms import UsuarioLoginForm


def dashboard(request):

    return render(request, 'usuario/dashboard.html')


def login(request):

    if request.method == 'POST':
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            usuario = Usuario()
            usuario.registro = form.cleaned_data['registro']
            usuario.senha = form.cleaned_data['senha']

            url = "https://servicos.conveniar.com.br/autenticacao/api/coordenador/oauth/token"
            r = requests.get(url,
                             )

            print(r.json())



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
