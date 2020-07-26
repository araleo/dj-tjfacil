from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect

from datetime import date, timedelta

from .forms import TaskForm
from .models import Task
from .util import cria_nova_task, define_times, get_min_date, bar_graph, line_graph, modifica_task


def detalhe(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    context = {"task": task, "form": TaskForm(instance=task)}

    try:
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect("timekeep:detalhe")
    except ValueError:
        context["error"] = "erro no input"

    return render(request, "timekeep/detalhe.html", context)


def perfil(request):

    if not request.user.is_authenticated:
        return redirect("timekeep:loginuser")

    t = Task.objects.filter(user=request.user)
    tasks = t.filter(
        completed__isnull=False,
        active=True,
        completed__range=(
            get_min_date(request),
            date.today() + timedelta(days=1)
        )
    ).order_by("-completed")

    times_delta, times_str, total_time = define_times(tasks)
    grafico_str = bar_graph(times_delta)
    grafico_lin = line_graph(t, 6)

    context = {
        "tasks": tasks,
        "totals": times_str,
        "total_time": total_time,
        "grafico": grafico_str,
        "grafico_lin": grafico_lin
    }
    return render(request, "timekeep/perfil.html", context)


def index(request):
    if not request.user.is_authenticated:
        return redirect("timekeep:loginuser")

    tasks = Task.objects.filter(user=request.user, completed__isnull=True, active=True)
    context = {"form": TaskForm(), "tasks": tasks}

    if request.method == "GET":
        return render(request, "timekeep/index.html", context)

    # inicio, pause, unpause e completar task
    if "task_pk" in request.POST:
        task = get_object_or_404(Task, pk=request.POST["task_pk"], user=request.user)
        modifica_task(request, task)

    # criação de nova task
    if "task" in request.POST:
        if not cria_nova_task(request):
            context["error"] = "erro no input"

    return redirect("timekeep:index")


def signupuser(request):
    if request.method == "GET":
        context = {"form": UserCreationForm()}
        return render(request, "timekeep/signupuser.html", context)

    if request.POST["password1"] != request.POST["password2"]:
        context = {"form": UserCreationForm(), "error": "senhas não conferem"}
        return render(request, "timekeep/signupuser.html", context)

    try:
        user = User.objects.create_user(
            request.POST["username"],
            password=request.POST["password1"]
        )
        user.save()
        login(request, user)
        return redirect("timekeep:index")
    except IntegrityError:
        context = {"form": UserCreationForm(), "error": "usuário já existe"}
        return render(request, "timekeep/signupuser.html", context)


def loginuser(request):
    if request.method == "GET":
        context = {"form": AuthenticationForm()}
        return render(request, "timekeep/loginuser.html", context)

    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

    if user is None:
        context = {"form": AuthenticationForm(), "error": "usuário ou senha incorretos"}
        return render(request, "timekeep/loginuser.html", context)

    login(request, user)
    return redirect("timekeep:index")


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("timekeep:loginuser")
