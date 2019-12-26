from django.db import models


class Empresa(models.Model):

    class Meta:
        db_table = 'empresa'

    razao_social = models.CharField(max_length=200)
    numero_inscricao = models.BigIntegerField()
    data_criacao = models.DateField(null=True)
    incricao_estadual = models.CharField(null=True, default='', max_length=200)

    def __str__(self):
        return self.razao_social




