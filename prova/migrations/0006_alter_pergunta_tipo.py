# Generated by Django 4.0 on 2021-12-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0005_pergunta_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='tipo',
            field=models.CharField(choices=[('D', 'Dissertatíva'), ('O', 'Optativa')], default=1, max_length=1),
        ),
    ]
