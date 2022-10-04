from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져옴!
    articles = Article.objects.order_by("-pk")
    # Template에 전달
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)


def create(request):
    # 글을 쓰고 나서 저장 되는 것!
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        # valid!
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        # get메서드 새로운 글 쓸때 사용됨
        article_form = ArticleForm()
    context = {
        # 객체가 돌아올 수 있도록 도와줌
        "article_form": article_form,
    }
    # invali!
    return render(request, "articles/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져옴
    article = Article.objects.get(pk=pk)
    # template에 객체 전옴
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)
