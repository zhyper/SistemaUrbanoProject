# Generated by Django 3.2.12 on 2022-07-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0031_zonaconsideracionesgenerales'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaObjetivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_zona', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_zona_objetivos',
                'managed': True,
            },
        ),
    ]
