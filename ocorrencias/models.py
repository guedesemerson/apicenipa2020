from django.db import models

class Ocorrencias(models.Model):
    codigo_ocorrencia = models.CharField(max_length=200)
    ocorrencia_classificacao = models.CharField(max_length=200)
    ocorrencia_tipo = models.CharField(max_length=200)
    ocorrencia_tipo_categoria = models.CharField(max_length=200)
    ocorrencia_tipo_icao = models.CharField(max_length=200)
    ocorrencia_latitude = models.CharField(max_length=200)
    ocorrencia_longitude = models.CharField(max_length=200)
    ocorrencia_cidade = models.CharField(max_length=200)
    ocorrencia_uf = models.CharField(max_length=200)
    ocorrencia_pais = models.CharField(max_length=200)
    ocorrencia_aerodromo = models.CharField(max_length=200)
    ocorrencia_dia = models.CharField(max_length=200)
    ocorrencia_horario = models.CharField(max_length=200)
    investigacao_aeronave_liberada = models.CharField(max_length=200)
    investigacao_status = models.CharField(max_length=200)
    divulgacao_relatorio_numero =  models.CharField(max_length=200)
    divulgacao_relatorio_publicado = models.CharField(max_length=200)
    divulgacao_dia_publicacao = models.CharField(max_length=200)
    total_recomendacoes= models.CharField(max_length=200)
    total_aeronaves_envolvidas = models.CharField(max_length=200)
    ocorrencia_saida_pista = models.CharField(max_length=200)
    ocorrencia_dia_extracao = models.CharField(max_length=200)

    def __str__(self):
        return self.ocorrencia_classificacao
