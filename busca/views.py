import string

from django.shortcuts import redirect, render

from .models import Tribunal
from .util import busca_tjfacil


def index(request):
    if request.method == "GET":
        return render(request, "busca/index.html")

    busca = request.POST["busca"]
    instancia = request.POST.get("instancia", "primeira")
    tipo = request.POST.get("eproc", "fisico")

    url = busca_tjfacil(busca, instancia, tipo)
    context = {"url": url}

    return redirect(url)
