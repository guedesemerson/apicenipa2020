# Generated by Django 2.2.10 on 2020-02-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fator',
            name='fator_area',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='fator',
            name='fator_aspecto',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='fator',
            name='fator_condicionante',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='fator',
            name='fator_detalhe_fator',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='fator',
            name='fator_dia_extracao',
            field=models.CharField(max_length=400),
        ),
    ]
