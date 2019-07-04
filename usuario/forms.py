from django import forms
from usuario.models import Usuario


class UsuarioLoginForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
            'registro': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'registro': "N° do Registro",
            'password': "Senha"
        }
