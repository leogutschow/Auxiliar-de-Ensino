# Generated by Django 4.0 on 2021-12-15 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_perfil_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='senha',
        ),
    ]