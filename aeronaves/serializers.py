from rest_framework.serializers import ModelSerializer
from .models import Aeronaves


class AreonavesSerializers(ModelSerializer):

    class Meta:
        model = Aeronaves
        fields= [ 'id',
                  'codigo_ocorrencia' ,
                  'aeronave_matricula',
                  'aeronave_operador_categoria',
                  'aeronave_tipo_veiculo',
                  'aeronave_fabricante',
                  'aeronave_modelo',
                  'aeronave_tipo_icao',
                  'aeronave_motor_tipo',
                  'aeronave_motor_quantidade',
                  'aeronave_pmd',
                  'aeronave_pmd_categoria',
                  'aeronave_assentos',
                  'aeronave_ano_fabricacao',
                  'aeronave_pais_fabricante',
                  'aeronave_pais_registro',
                  'aeronave_registro_categoria',
                  'aeronave_registro_segmento',
                  'aeronave_voo_origem',
                  'aeronave_voo_destino',
                  'aeronave_fase_operacao',
                  'aeronave_fase_operacao_icao',
                  'aeronave_tipo_operacao',
                  'aeronave_nivel_dano',
                  'total_fatalidades',
                  'aeronave_dia_extracao']