# Generated by Django 3.2.12 on 2022-06-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0008_auto_20220630_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='slug',
            field=models.SlugField(default=None, max_length=250, null=True),
        ),
    ]