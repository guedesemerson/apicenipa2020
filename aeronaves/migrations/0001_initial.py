# Generated by Django 2.2.10 on 2020-02-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeronaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ocorrencia', models.CharField(max_length=150)),
                ('aeronave_matricula', models.CharField(max_length=150)),
                ('aeronave_operador_categoria', models.CharField(max_length=150)),
                ('aeronave_tipo_veiculo', models.CharField(max_length=150)),
                ('aeronave_fabricante', models.CharField(max_length=150)),
                ('aeronave_modelo', models.CharField(max_length=150)),
                ('aeronave_tipo_icao', models.CharField(max_length=150)),
                ('aeronave_motor_tipo', models.CharField(max_length=150)),
                ('aeronave_motor_quantidade', models.CharField(max_length=150)),
                ('aeronave_pmd', models.CharField(max_length=150)),
                ('aeronave_pmd_categoria', models.CharField(max_length=150)),
                ('aeronave_assentos', models.CharField(max_length=150)),
                ('aeronave_ano_fabricacao', models.CharField(max_length=150)),
                ('aeronave_pais_fabricante', models.CharField(max_length=150)),
                ('aeronave_pais_registro', models.CharField(max_length=150)),
                ('aeronave_registro_categoria', models.CharField(max_length=150)),
                ('aeronave_registro_segmento', models.CharField(max_length=150)),
                ('aeronave_voo_origem', models.CharField(max_length=150)),
                ('aeronave_voo_destino', models.CharField(max_length=150)),
                ('aeronave_fase_operacao', models.CharField(max_length=150)),
                ('aeronave_fase_operacao_icao', models.CharField(max_length=150)),
                ('aeronave_tipo_operacao', models.CharField(max_length=150)),
                ('aeronave_nivel_dano', models.CharField(max_length=150)),
                ('total_fatalidades', models.CharField(max_length=300)),
                ('aeronave_dia_extracao', models.CharField(max_length=300)),
            ],
        ),
    ]