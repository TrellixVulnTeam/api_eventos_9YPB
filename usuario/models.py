from django.db import models


# Create your models here.
class Usuario(models.Model):
    registro = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return self.registro
