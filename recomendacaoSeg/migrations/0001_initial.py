# Generated by Django 2.2.10 on 2020-02-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecomendacaoSeg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ocorrencia', models.CharField(max_length=300)),
                ('recomendacao_numero', models.CharField(max_length=300)),
                ('recomendacao_dia_assinatura', models.CharField(max_length=300)),
                ('recomendacao_dia_encaminhamento', models.CharField(max_length=300)),
                ('recomendacao_feedback', models.CharField(max_length=300)),
                ('recomendacao_conteudo', models.CharField(max_length=300)),
                ('recomendacao_status', models.CharField(max_length=300)),
                ('recomendacao_destinatario_sigla', models.CharField(max_length=300)),
                ('recomendacao_destinatario_nome', models.CharField(max_length=300)),
                ('dia_extracao_recomendacao', models.CharField(max_length=300)),
            ],
        ),
    ]
