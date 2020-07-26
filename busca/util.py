import string

from .models import Tribunal


def busca_tjfacil(busca, instancia, tipo):
    """Recebe três strings e retorna a url buscada"""
    if busca[0] in string.ascii_letters:
        return busca_sigla(busca)

    if instancia_superior(instancia):
        return busca_superiores(instancia, tipo)

    return busca_numero(busca, instancia, tipo)


def busca_superiores(instancia, tipo):
    """Recebe duas strings e retorna url"""
    tribunal = Tribunal.objects.get(sigla=instancia.upper())
    return tribunal.get_site("primeira", tipo)


def busca_sigla(sigla):
    """Recebe uma string e retorna url"""
    tribunal = Tribunal.objects.get(sigla=sigla.upper())
    return tribunal.site_principal


def busca_numero(numero, instancia, tipo):
    """Recebe três strings e retorna url"""
    codigo = get_codigo(numero)
    tribunal = Tribunal.objects.get(codigo=codigo)
    return tribunal.get_site(instancia, tipo)


def get_codigo(numero):
    """
    Recebe uma string referente a um numero de processo
    Retorna uma string referente a um código de tribunal
    """
    numero = strip_num(numero)
    codigo, regiao = numero[13:16], numero[16:18]
    codigo = codigo + regiao if codigo.startswith("4") else codigo
    return codigo


def strip_num(numero):
    """
    Recebe uma string representando um numero de processo
    Retorna uma string representando o mesmo numero de processo
    sem pontos, virgulas, traços, etc e com 0s a esquerda até 20 casas
    """
    return "".join([n for n in numero if n in string.digits]).zfill(20)


def instancia_superior(instancia):
    """
    Recebe uma string representando a instancia
    retorna verdadeiro se instancia = STF, STJ ou TST
    """
    instancia = instancia.upper()
    return instancia == "STJ" or instancia =="STF" or instancia == "TST"
