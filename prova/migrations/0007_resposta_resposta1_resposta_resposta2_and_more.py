# Generated by Django 4.0 on 2021-12-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0006_alter_pergunta_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='resposta1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta3',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta4',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta5',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta6',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta7',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='resposta',
            name='resposta8',
            field=models.CharField(default='', max_length=500),
        ),
    ]