from multiprocessing import context
from urllib import request
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import articles
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
        ppap_form = ReviewForm(request.POST, request.FILES)
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
    context = {
        "i": k,
    }
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
            ppap_form = ReviewForm(request.POST, request.FILES, instance=k)
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


def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Review, pk=article_pk)

        # 해당 게시글을 좋아요한 사람중에 pk가 현재 유저의 pk랑 같은 것이
        # 존재하는지 하지 않는지 판단
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect("articles:index")
    return redirect("accouts:login")
