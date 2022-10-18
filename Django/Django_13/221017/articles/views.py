from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from articles.forms import ReviewForm
from .models import Review
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    k = Review.objects.all().order_by("id")
    page = request.GET.get("page", "1")  # 페이지
    paginator = Paginator(k, 6)
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
            messages.warning(request, "글 작성이 완료되었습니다.")
            return redirect("/", article.pk)

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
    # 1. 모델의 예외 대신 발생
    # 2. 만약 객체가 존재하지 않을 때 get() 을 사용하여 Http404 예외를 발생시키는것
    # 3. Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘긴다.
    k = get_object_or_404(Review, pk=pk)
    # k = Review.objects.get(pk=pk)
    if request.user == k.user:
        if request.method == "POST":
            ppap_form = ReviewForm(request.POST, request.FILES, instance=k)
            if ppap_form.is_valid():
                ppap_form.save()
                messages.warning(request, "글이 수정되었습니다.")
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


def search(request):
    if request.method == "GET":
        content_list = Review.objects.all()
        search = request.GET.get("search", "")

        if search:
            search_list = content_list.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
            return render(request, "articles/search.html", {"search": search_list})
