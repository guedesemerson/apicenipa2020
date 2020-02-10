from rest_framework.serializers import ModelSerializer
from .models import Ocorrencias

class OcorrenciaSerializers(ModelSerializer):
    class Meta:
        model = Ocorrencias
        fields =["id","codigo_ocorrencia","ocorrencia_classificacao","ocorrencia_tipo","ocorrencia_tipo_categoria"
                      ,"ocorrencia_tipo_icao","ocorrencia_latitude","ocorrencia_longitude","ocorrencia_cidade","ocorrencia_uf",
                      "ocorrencia_pais","ocorrencia_aerodromo","ocorrencia_dia","ocorrencia_horario","investigacao_aeronave_liberada"
                      ,"investigacao_status","divulgacao_relatorio_numero","divulgacao_relatorio_publicado","divulgacao_dia_publicacao"
                      ,"total_recomendacoes","total_aeronaves_envolvidas","ocorrencia_saida_pista","ocorrencia_dia_extracao"]