# Generated by Django 3.2.12 on 2022-08-31 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0011_auto_20220831_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodataitem',
            name='etapa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zonas.planetapa'),
        ),
    ]
