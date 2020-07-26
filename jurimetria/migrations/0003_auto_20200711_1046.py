# Generated by Django 3.0.7 on 2020-07-11 13:46

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurimetria', '0002_sentenca_search_vector'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='sentenca',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='search_vector_idx'),
        ),
    ]
