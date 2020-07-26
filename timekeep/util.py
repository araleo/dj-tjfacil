import base64
import urllib
from datetime import date, datetime, timedelta
from io import BytesIO

import matplotlib
import matplotlib.pyplot as plt
from django.utils import timezone

from .forms import TaskForm
from .models import Task


def cria_nova_task(request):
    """
    Recebe um request com uma task
    para criação no banco de dados
    Retorna booleano para sucesso/erro
    """
    try:
        form = TaskForm(request.POST)
        newtask = form.save(commit=False)
        newtask.user = request.user
        newtask.save()
        return True
    except ValueError:
        return False


def modifica_task(request, task):
    """
    Recebe o request e uma task
    Modifica a task no banco de dados
    de acordo com as instruções do request
    """
    if "botaoinicio" in request.POST:
        task.start = timezone.now()
        task.save()

    elif "botaopause" in request.POST:
        if task.pause_begin is None:
            task.pause_begin = timezone.now()
            task.save()

    elif "botaounpause" in request.POST:
        time_paused = timezone.timedelta(0)
        if task.paused is not None:
            time_paused = task.paused
        task.paused = time_paused + (timezone.now() - task.pause_begin)
        task.pause_begin = None
        task.save()

    elif "botaocompletar" in request.POST:
        task.completed = timezone.now()
        task.elapsed = task.completed - task.start - task.paused
        task.elapsed_str = time_to_str(task.elapsed)
        task.save()

    elif "botaoexcluir" in request.POST:
        task.active = False
        task.save()


def next_sunday():
    """Retorna um datetime do próximo domingo ou do dia atual, se for domingo"""
    data = date.today()
    while data.weekday() != 6:
        data += timedelta(days=1)
    return data


def ultimos_domingos(domingo, num):
    """Retorna uma lista com datetime dos num ultimos domingos"""
    return [domingo - timedelta(days=x*7) for x in range(num)]


def get_tasks_in_range(tasks, min_date, max_date):
    """
    Recebe um grupo de objetos Task, e duas datas
    Retorna um QuerySet de tasks filtrado entre as datas
    """
    return tasks.filter(
        completed__isnull=False,
        active=True,
        completed__range=(min_date, max_date)
    ).order_by("-completed")


def get_times_in_week(domingos, tasks):
    """
    Recebe uma lista com datetimes de domingos
    Retorna uma lista com o tempo total gasto
    em todas as tasks entre cada domingo
    """
    tempos = []
    for domingo in domingos:
        t = get_tasks_in_range(tasks, domingo - timedelta(days=6), domingo + timedelta(days=1))
        delta_totals = delta_totals_dict(t)
        total_time = sum(delta_totals.values(), timedelta())
        tempos.append(total_time)
    return tempos


def line_graph(tasks, num):
    """
    Recebe um QuerySet de tasks e um inteiro
    Retorna uma url para buffer de um grafico em linha onde
    x = num ultimas semanas
    y = tempo total em todas as tasks em cada semana
    """
    proximo_domingo = next_sunday()
    domingos = ultimos_domingos(proximo_domingo, num)
    tempos = get_times_in_week(domingos, tasks)
    tempos_minutos = [t.total_seconds() // 60 for t in tempos][::-1]
    semanas = [domingo.strftime("%d-%m-%Y") for domingo in domingos][::-1]
    return graph(semanas, tempos_minutos, "minutos", "Produtividade por semana", tipo="lin")


def bar_graph(totals):
    """
    Recebe um dicionário totals = {task: elapsed}
    Retorna a url para buffer de um grafico de barras onde
    x = tasks agrupadas
    y = tempo gasto
    """
    labs = sorted(totals, key=totals.get, reverse=True)
    vals = sorted([totals[x].total_seconds() / 60 for x in totals], reverse=True)
    return graph(labs[:6], vals[:6], "minutos", "Total por tarefa (no período escolhido)")


def graph(x, y, ylabel, title, tipo="bar"):
    """Se tipo == lin traça um gráfico de linha"""
    matplotlib.use('Agg')

    # grafico
    plt.figure(figsize=(7, 5))
    if tipo == "lin":
        plt.plot(x, y, color="#80A1C1")
    else:
        plt.bar(x, y, color="#80A1C1", width=0.8)
    plt.xticks(rotation=45)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()

    # salva em buffer e converte em string
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    return urllib.parse.quote(string)


def get_min_date(request):
    """Recebe um request e retorna o período de tempo selecionado pelo usuário"""
    if "botao-7d" in request.POST:
        days = 7
    elif "botao-30d" in request.POST:
        days = 30
    elif "botao-inicio" in request.POST:
        days = 365 * 10
    else:
        days = 0
    return date.today() - timedelta(days=days)


def delta_totals_dict(tasks):
    """
    Recebe um QuerySet de tasks
    Retorna um dicionário delta_totals = {task: elapsed}
    """
    delta_totals = dict()
    for task in tasks:
        k = task.task.lower()
        delta_totals.setdefault(k, timedelta(0))
        delta_totals[k] += task.elapsed
    return delta_totals


def human_totals_dict(delta_totals):
    """Humaniza um dicionário {task: elapsed}"""
    return {
        task: time_to_str(delta_totals[task])
        for task in delta_totals
    }


def define_times(tasks):
    """
    Recebe um QuerySet de tasks
    Retorna dois dicionários
    delta_totals = {task: elapsed}
    human_totals = {task: humanized(elapsed)}
    e uma string com o tempo total gasto em tasks humanizado
    """
    delta_totals = delta_totals_dict(tasks)
    human_totals = human_totals_dict(delta_totals)
    total_time = str_time_to_pt(sum(delta_totals.values(), timedelta()))
    return delta_totals, human_totals, total_time


def str_time_to_pt(delta):
    """Recebe um timedelta e retorna uma string formatada"""
    total_secs = delta.total_seconds()
    m, _ = divmod(total_secs, 60)
    h, m = divmod(m, 60)
    h, m = str(int(h)), str(int(m))
    min = "minuto" if m == "1" else "minutos"
    hora = "hora" if h == "1" else "horas"
    minutos = f"{m} {min}" if m != "0" else ""
    horas = f"{h} {hora}" if h != "0" else ""
    con = f" e " if h != "0" and m != "0" else ""
    pt = f"{horas}{con}{minutos}"
    return pt


def time_to_str(time):
    """Recebe um timedelta e retorna uma string formatada"""
    time_str = str(time).split(":")
    return f"{time_str[0]}:{time_str[1]}"


def main():
    pass


if __name__ == "__main__":
    main()
