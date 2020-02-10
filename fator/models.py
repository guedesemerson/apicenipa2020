from django.db import models

class Fator(models.Model):
    codigo_ocorrencia = models.CharField(max_length=150)
    fator_nome = models.CharField(max_length=150)
    fator_aspecto = models.CharField(max_length=400)
    fator_condicionante= models.CharField(max_length=400)
    fator_area = models.CharField(max_length=400)
    fator_detalhe_fator = models.CharField(max_length=400)
    fator_dia_extracao = models.CharField(max_length=400)
    def __str__(self):
        return self.fator_nome
