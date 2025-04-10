# Generated by Django 5.2 on 2025-04-09 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='requerimientos_sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema', models.CharField(max_length=100)),
                ('procesador', models.CharField(max_length=100)),
                ('memoria', models.CharField(max_length=50)),
                ('grafica', models.CharField(max_length=100)),
                ('almacenamiento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=50)),
                ('imagen', models.URLField()),
                ('descripcion_pequeña', models.CharField(max_length=200)),
                ('descricpcion', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('editor', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('game_url', models.URLField(blank=True, null=True)),
                ('requerimientos_sistema', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='games.requerimientos_sistema')),
            ],
        ),
    ]
