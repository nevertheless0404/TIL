from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from articles.forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.core.paginator import Paginator

# from xml.etree.ElementTree import Comment

# Create your views here.


def index(request):
    k = Review.objects.all().order_by("id")
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
    comment_form = CommentForm()
    comments = k.comment_set.all()
    context = {
        "i": k,
        "comment_form": comment_form,
        "comments": comments,
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


def comment_create(request, article_pk):
    article = Review.objects.get(pk=article_pk)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            messages.success(request, "댓글 추가 완료")
    else:
        messages.warning(request, "잘못된 접근입니다.")
    return redirect("articles:detail", article.pk)


def comment_update(request, article_pk, comment_pk):
    article = Review.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)

    if request.user != comment.user:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article.pk)

    if request.method == "POST":
        updated_comment = request.POST.get("updated_comment")
        if 0 < len(updated_comment) <= 80:
            comment.content = updated_comment
            comment.article = article
            comment.save()
            messages.success(request, "댓글 수정 완료")
    else:
        messages.warning(request, "잘못된 접근입니다.")
    return redirect("articles:detail", article.pk)


def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user != comment.user:
        messages.warning(request, "권한이 없습니다.")
        return redirect("articles:detail", article_pk)
    if request.method == "POST":
        comment.delete()
        messages.warning(request, "댓글 삭제 완료")
    else:
        messages.warning(request, "잘못된 접근입니다.")
    return redirect("articles:detail", article_pk)
