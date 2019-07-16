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
