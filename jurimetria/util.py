from .rol_varas import VARAS_NOMES


def coloca_acento(tipo):
    """Transforma absolutórias->absolutórias e condenatorias->condenatórias"""
    if tipo == "absolutorias":
        return "absolutórias"
    elif tipo == "condenatorias":
        return "condenatórias"
    else:
        return tipo


def formata_numero_cnj(n):
    """
    Recebe uma string representando um numero de processo
    Retorna uma string com o numero no formato CNJ
    """
    return f"{n[:7]}-{n[7:9]}.{n[9:13]}.{n[13]}.{n[14:16]}.{n[16:20]}"


def query_counts(categorias):
    """
    Recebe um QuerySet contendo categorias: quantidade
    Retorna um dicionário counts = {categoria: quantidade, }
    """
    counts = {d["tipo"]: d["count"] for d in categorias}
    return counts


def get_post_query_input(request):
    """Recebe um request e retorna os argumentos da busca do usuário"""
    vara = request.POST["select-vara"]
    tipo = request.POST["select-tipo"]
    busca = request.POST["query"]
    return vara, tipo, busca


def set_out_pcts(vals):
    """
    Recebe um dicionário vals = {tipo: quantidade}
    Retorna um dicionário pcts = {tipo: porcentagem}
    """
    total = sum(vals.values())
    pcts = {}
    for k in vals:
        pcts[k] = vals[k] / total * 100
    return pcts


def set_out_values(counts):
    """
    Recebe um dicionário counts = {tipo: quantidade}
    Retorna um dicionário vals = {tipo: quantidade}
    incluindo tipos com count = 0
    """
    tipos = ["absolutorias", "condenatorias", "neutras"]
    vals = {}
    for tipo in tipos:
        val = counts.get(tipo, 0)
        vals[tipo] = val
    return vals


def make_output_tuple(counts, query, query_count, vara):
    """
    Recebe um dicionário counts = {tipo: quantidade}
    uma string com a expressão buscada
    um inteiro com a quantidade de resultados
    e uma string com o nome da vara buscada
    Retorna uma tupla com duas strings formatadas para output
    uma com valores absolutos e outra com porcentagens
    """
    vals = set_out_values(counts)
    pcts = set_out_pcts(vals)
    query_qtd = format_query_qtd(query, query_count, vara)
    vals_pcts = format_vals_pcts(vals, pcts)
    return query_qtd, vals_pcts


def format_vals_pcts(vals, pcts):
    """Recebe dois dicionários e retorna uma string formatada para output"""
    return "\n".join((
        f"{vals['absolutorias']} absolutórias ({pcts['absolutorias']:.2f}%)",
        f"{vals['condenatorias']} condenatórias ({pcts['condenatorias']:.2f}%)",
        f"{vals['neutras']} neutras ({pcts['neutras']:.2f}%)",
    ))


def format_query_qtd(query, query_count, vara):
    """Recebe duas strings e um inteiro retorna uma string formatada para output"""
    return "".join((
        f"Foram encontradas {query_count} sentenças ",
        f"contendo o termo {query} ",
        f"na {VARAS_NOMES[vara]}. "
    ))
