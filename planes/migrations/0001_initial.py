# Generated by Django 3.2.12 on 2022-07-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParametroUrbanoPDU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_area', models.CharField(max_length=100)),
                ('cod_tipo_area', models.CharField(max_length=100)),
                ('tipo_zona', models.CharField(max_length=100)),
                ('cod_tipo_zona', models.CharField(max_length=100)),
                ('zona', models.CharField(max_length=100)),
                ('cod_zona', models.CharField(max_length=100)),
                ('usos', models.CharField(max_length=100)),
                ('densidad_neta', models.IntegerField()),
                ('lote_minimo', models.IntegerField()),
                ('frente_minimo', models.IntegerField()),
                ('altura_edifica', models.CharField(max_length=100)),
                ('coeficiente_edifica', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area_edifica', models.IntegerField()),
                ('area_libre', models.IntegerField()),
                ('estacionamiento', models.CharField(max_length=100)),
                ('nivel_servicio', models.CharField(max_length=100)),
                ('lote_frente_minimo', models.CharField(max_length=100)),
                ('residencial_compatible', models.CharField(max_length=100)),
                ('agno_aprobacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Parametro PDU',
                'verbose_name_plural': 'Parametros PDU',
                'db_table': 't_parametro_urbano_pdu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MapaWeb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mapa Web',
                'verbose_name_plural': 'Mapas Web',
                'db_table': 't_mapa_web',
                'managed': True,
            },
        ),
    ]
