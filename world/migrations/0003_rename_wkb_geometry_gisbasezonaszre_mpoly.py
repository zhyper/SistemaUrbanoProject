# Generated by Django 3.2.12 on 2022-03-28 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_alter_gisbasezonaszre_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gisbasezonaszre',
            old_name='wkb_geometry',
            new_name='mpoly',
        ),
    ]
