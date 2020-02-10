from django.db import models

class RecomendacaoSeg(models.Model):
    codigo_ocorrencia = models.CharField(max_length=300)
    recomendacao_numero = models.CharField(max_length=300)
    recomendacao_dia_assinatura = models.CharField(max_length=300)
    recomendacao_dia_encaminhamento = models.CharField(max_length=300)
    recomendacao_feedback = models.CharField(max_length=500)
    recomendacao_conteudo = models.CharField(max_length=500)
    recomendacao_status = models.CharField(max_length=300)
    recomendacao_destinatario_sigla = models.CharField(max_length=300)
    recomendacao_destinatario_nome = models.CharField(max_length=300)
    dia_extracao_recomendacao = models.CharField(max_length=300)
    def __str__(self):
        return self.recomendacao_numero
