from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Noticia(models.Model):
    portal = models.CharField(max_length=100)
    data = models.DateField()
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    link = models.URLField()
    tipo = models.CharField(max_length=50, blank=True)
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return f"{self.portal} | {self.titulo}"

    class Meta:
        indexes = [GinIndex(fields=["search_vector"], name="noticias_search_vector_idx")]
