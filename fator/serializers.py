from rest_framework.serializers import ModelSerializer
from .models import Fator

class FatorSerializers(ModelSerializer):
    class Meta:
        model = Fator
        fields =["id","codigo_ocorrencia", "fator_nome", "fator_aspecto", "fator_condicionante", "fator_area",
                   "fator_detalhe_fator", "fator_dia_extracao"]