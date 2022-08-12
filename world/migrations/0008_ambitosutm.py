# Generated by Django 3.2.12 on 2022-03-28 19:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0007_ambitos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambitosutm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('admapkey', models.FloatField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32719)),
            ],
        ),
    ]
