from django.db import models


# Create your models here.
class Usuario(models.Model):
    registro = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    token = models.CharField(max_length=700)

    class Meta:
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.registro


# class UsuarioCadatro(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField(max_length=80)
#     senha = models.CharField(max_length=70)
#     cracha = models.CharField(max_length=70)
#     Documento = models.CharField(max_length=20)
#     Sexo = models.CharField(max_length=1)
#     TelefoneCelular = models.CharField(max_length=20)
#     TelefoneCasa = models.CharField(max_length=20)
#     TelefoneEmpresa = models.CharField(max_length=20)
#     CEP = models.CharField(max_length=20)
#     Endereco = models.CharField(max_length=70)
#     Bairro = models.CharField(max_length=70)
#     Cidade = models.CharField(max_length=70)
#     Estado = models.CharField(max_length=70)
#     Pais = models.CharField(max_length=70)
#
#     class Meta:
#         verbose_name_plural = 'usuarios'
#
#     def __str__(self):
#         return self.nome
