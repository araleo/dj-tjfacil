from datetime import datetime


def load_input(post):
    query = post["query"]
    tipo = load_tipo(post["select-tipo"])
    data_inicio = load_date(post["data-inicio"])
    data_fim = load_date(post["data-fim"])
    return query, tipo, data_inicio, data_fim


def load_date(data):
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        data = ""
    return data


def load_tipo(tipo):
    return "" if tipo == "todos" else tipo


def classify_noticias(noticias):
    """
    Recebe um QuerySet de noticias e retorna um dicionario
    no formato {tipo: {data: {portal: []}}}
    """
    news = {}
    for noticia in noticias:
        news.setdefault(noticia.tipo, {})
        news[noticia.tipo].setdefault(noticia.data, {})
        news[noticia.tipo][noticia.data].setdefault(noticia.portal, [])
        news[noticia.tipo][noticia.data][noticia.portal].append(noticia)
    return news
