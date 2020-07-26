from django.contrib.postgres.search import SearchQuery, SearchRank
from django.db.models import Count, F
from django.shortcuts import get_object_or_404, redirect, render

from unidecode import unidecode

from .models import Sentenca
from .rol_varas import VARAS_NOMES
from .util import coloca_acento, formata_numero_cnj, get_post_query_input, make_output_tuple, query_counts


def index(request):
    if request.method == "GET":
        return render(request, "jurimetria/index.html")


def result(request):
    if request.method == "GET":
        return redirect("jurimetria:index")

    vara, tipo, busca = get_post_query_input(request)
    query = SearchQuery(unidecode(busca), config="portuguese")

    sents = Sentenca.objects.filter(vara=vara, search_vector=query)

    if len(sents) == 0:
        context = {"erro": "Não há sentenças com os filtros selecionados."}
        return render(request, "jurimetria/index.html", context)

    sentencas = sents.filter(tipo=tipo)
    sents_rank = sentencas.annotate(rank=SearchRank(F("search_vector"), query)).order_by("-rank")[:10]

    categorias = sents.order_by("tipo").values("tipo").annotate(count=Count("tipo"))
    cat_counts = query_counts(categorias)
    query_count = len(sents)

    query_qtd, vals_pcts = make_output_tuple(cat_counts, busca, query_count, vara)

    context = {"sentencas": sents_rank, "query": query_qtd, "vals": vals_pcts, "tipo": coloca_acento(tipo)}

    return render(request, "jurimetria/result.html", context)


def detail(request, sentenca_id):
    sentenca = get_object_or_404(Sentenca, pk=sentenca_id)
    sentenca.numero = formata_numero_cnj(sentenca.numero)
    sentenca.vara = VARAS_NOMES[sentenca.vara]
    sentenca.tipo = coloca_acento(sentenca.tipo)
    context = {"sentenca": sentenca}
    return render(request, "jurimetria/detail.html", context)
