# Generated by Django 3.2.12 on 2022-09-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0014_alter_tzona_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tzona',
            name='tipo_zre',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
