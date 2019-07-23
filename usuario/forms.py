from django import forms
from usuario.models import Usuario


class UsuarioLoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['token']

        widgets = {
            'registro': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'})
        }

        labels = {
            'registro': "N° do Registro",
            'password': "Senha"
        }


# class UsuarioCadastroLoginForm(forms.ModelForm):
#     class Meta:
#         model = UsuarioCadatro
#         exclude = ['']
#
#         widgets = {
#             'nome': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.TextInput(attrs={'class': 'form-control'}),
#             'senha': forms.TextInput(attrs={'class': 'form-control'}),
#             'cracha': forms.TextInput(attrs={'class': 'form-control'}),
#             'Documento': forms.TextInput(attrs={'class': 'form-control'}),
#             'Sexo': forms.TextInput(attrs={'class': 'form-control'}),
#             'TelefoneCelular': forms.TextInput(attrs={'class': 'form-control'}),
#             'TelefoneCasa': forms.TextInput(attrs={'class': 'form-control'}),
#             'TelefoneEmpresa': forms.TextInput(attrs={'class': 'form-control'}),
#             'CEP': forms.TextInput(attrs={'class': 'form-control'}),
#             'Endereco': forms.TextInput(attrs={'class': 'form-control'}),
#             'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
#             'Cidade': forms.TextInput(attrs={'class': 'form-control'}),
#             'Estado': forms.TextInput(attrs={'class': 'form-control'}),
#             'Pais': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#
#         labels = {
#             'nome': 'Nome',
#             'email': 'Email',
#             'senha': 'Senha',
#             'cracha': 'Crachá',
#             'Documento': 'Documento',
#             'Sexo': 'Sexo',
#             'TelefoneCelular': 'Telefone Celular',
#             'TelefoneCasa': 'Telefone Casa',
#             'TelefoneEmpresa': 'Telefone Empresa',
#             'CEP': 'CEP',
#             'Endereco': 'Enderenço',
#             'Bairro': 'Bairro',
#             'Cidade': 'Cidade',
#             'Estado': 'Estado',
#             'Pais': 'Pais',
#         }
