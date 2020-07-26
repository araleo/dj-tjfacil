from datetime import date 

from django.contrib.postgres.search import SearchQuery
from django.shortcuts import render

from .models import Noticia
from .util import classify_noticias, load_input


def index(request):

    if request.method == "GET":
        noticias = Noticia.objects.filter(data=date.today())

    if request.method == "POST":
        busca, tipo, data_inicio, data_fim = load_input(request.POST)
        query = SearchQuery(busca)

        noticias = Noticia.objects.all()
        noticias = noticias.filter(tipo=tipo) if tipo else noticias
        noticias = noticias.filter(data__gte=data_inicio) if data_inicio else noticias
        noticias = noticias.filter(data__lte=data_fim) if data_fim else noticias
        noticias = noticias.filter(search_vector=query) if busca else noticias
        noticias = noticias.order_by("-data")

    context = {"noticias": classify_noticias(noticias)}
    return render(request, "noticias/index.html", context)
