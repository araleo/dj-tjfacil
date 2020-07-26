from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import models


class Sentenca(models.Model):
    tribunal = models.CharField(max_length=50)
    vara = models.CharField(max_length=50)
    numero = models.CharField(max_length=30)
    texto = models.TextField()
    decoded = models.TextField()
    tipo = models.CharField(max_length=20)
    pub_date = models.DateTimeField("data publicacao", null=True, blank=True)
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.numero

    class Meta:
        indexes = [GinIndex(fields=["search_vector"], name="jurimetria_search_vector_idx")]
