# Generated by Django 4.0.4 on 2022-11-23 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_perfil_foto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='foto',
        ),
    ]
