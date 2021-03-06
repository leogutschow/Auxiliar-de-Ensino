# Generated by Django 4.0 on 2021-12-23 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0004_alter_prova_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_texto', models.TextField()),
                ('tipo', models.CharField(choices=[(1, 'Dissertatíva'), (2, 'Optativa')], default=1, max_length=1)),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.prova')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.pergunta')),
            ],
        ),
    ]
