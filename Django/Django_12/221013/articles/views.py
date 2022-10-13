from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
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
            article = ppap_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("/", article.pk)
        messages.add_message(request, messages.INFO, "정보를 나타냅니다.")
    else:
        ppap_form = ReviewForm()
    context = {
        "ppap_form": ppap_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"i": k,}
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def update(request, pk):
    k = get_object_or_404(Review, pk=pk)
    # k = Review.objects.get(pk=pk)
    if request.user == k.user:
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
