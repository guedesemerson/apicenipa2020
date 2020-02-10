from rest_framework.serializers import ModelSerializer
from .models import RecomendacaoSeg

class RecomendacaoSegSerializers(ModelSerializer):
    class Meta:
        model = RecomendacaoSeg
        fields =["id","codigo_ocorrencia", "recomendacao_numero", "recomendacao_dia_assinatura", "recomendacao_dia_encaminhamento",
        "recomendacao_feedback", "recomendacao_conteudo", "recomendacao_status",
        "recomendacao_destinatario_sigla", "recomendacao_destinatario_nome", "dia_extracao_recomendacao"]