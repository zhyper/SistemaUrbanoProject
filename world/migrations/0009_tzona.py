# Generated by Django 3.2.12 on 2022-04-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0008_ambitosutm'),
    ]

    operations = [
        migrations.CreateModel(
            name='TZona',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_zona', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=10)),
                ('zoom', models.DecimalField(decimal_places=10, max_digits=10)),
                ('observacion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_zona',
            },
        ),
    ]