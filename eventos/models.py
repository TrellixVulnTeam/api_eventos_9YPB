from django.db import models


# Create your models here.
class Eventos(models.Model):
    CodEvento = models.IntegerField()
    NomeEvento = models.CharField(max_length=255)
    NomeConvenio = models.CharField(max_length=255)
    Categoria = models.CharField(max_length=40)
    Situacao = models.CharField(max_length=40)
    DataInicio = models.DateTimeField()
    DataFim = models.DateTimeField()
    NumeroVagas = models.IntegerField()
    NomeEventoInformacao = models.CharField(max_length=255)
    DescricaoEventoInformacao = models.CharField(max_length=255)

    def __str__(self):
        return self.NomeEvento

    class Meta:
        verbose_name_plural = 'Eventos'
