from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from articles.forms import ReviewForm
from .models import Review
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    k = Review.objects.order_by("id")
    page = request.GET.get("page", "1")  # 페이지
    paginator = Paginator(k, 3)
    page_obj = paginator.get_page(page)
    context = {
        "v": k,
        "question_list": page_obj,
    }

    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        ppap_form = ReviewForm(request.POST)
        if ppap_form.is_valid():
            ppap_form.save()
            return redirect("/")
        messages.add_message(request, messages.INFO, "정보를 나타냅니다.")
    else:
        ppap_form = ReviewForm()
    context = {
        "ppap_form": ppap_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"i": k}
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("/")


def update(request, pk):
    k = Review.objects.get(pk=pk)
    if request.method == "POST":
        ppap_form = ReviewForm(request.POST, instance=k)
        if ppap_form.is_valid():
            ppap_form.save()
            return redirect("/", k.pk)
    else:
        ppap_form = ReviewForm(instance=k)
    context = {
        "ppap_form": ppap_form,
        "ppap": k,
    }
    return render(request, "articles/update.html", context)
