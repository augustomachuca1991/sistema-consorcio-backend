# Generated by Django 5.0.6 on 2024-07-03 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_id_permiso_user_id_tipousuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_permiso',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_tipoUsuario',
        ),
    ]
