# Generated by Django 3.0.7 on 2020-07-05 04:09

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurimetria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentenca',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]