# Generated by Django 3.0.7 on 2020-07-16 19:08

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]