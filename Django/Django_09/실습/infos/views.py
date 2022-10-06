from multiprocessing import context
from django.shortcuts import render, redirect
from infos.forms import InfosForm
from .models import Infos

# Create your views here.
def movies(request):
    k = Infos.objects.order_by("id")
    context = {
        "v": k,
    }
    return render(request, "infos/movies.html", context)


def create(request):
    if request.method == "POST":
        infos_form = InfosForm(request.POST)
        if infos_form.is_valid():
            infos_form.save()
            return redirect("infos:movies")
    else:
        infos_form = InfosForm()
    context = {
        "infos_form": infos_form,
    }
    return render(request, "infos/create.html", context)


def detail(request, pk):
    k = Infos.objects.get(pk=pk)
    context = {
        "i": k,
    }
    return render(request, "infos/detail.html", context)


def delete(request, pk):
    Infos.objects.get(pk=pk).delete()
    return redirect("infos:movies")


def update(request, pk):
    k = Infos.objects.get(pk=pk)
    if request.method == "POST":
        infos_form = InfosForm(request.POST, instance=k)
        if infos_form.is_valid():
            infos_form.save()
            return redirect("infos:detail", k.pk)
    else:
        infos_form = InfosForm(instance=k)
    context = {
        "infos_form": infos_form,
        "infos": k,
    }

    return render(request, "infos/update.html", context)
