from django.contrib import messages
from django.shortcuts import redirect, render
from articles.forms import ReviewForm
from .models import Review


# Create your views here.


def index(request):
    k = Review.objects.order_by("id")
    context = {
        "v": k,
    }
    return render(request, "articles/index.html", context)


def create(request):
    # if request.method == "GET":
    #     k = request.GET
    #     context = {"k": k}

    #     return render(request, "articles/create.html", context)
    # else:

    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     Review.objects.create(title=title, content=content)

    #     return redirect("/")
    if request.method == "POST":
        ppap_form = ReviewForm(request.POST)
        if ppap_form.is_valid():
            ppap_form.save()
            return redirect("/")
        messages.add_message(request, messages.INFO, "정보를 나타냅니다.")
    else:
        ppap_form = ReviewForm()
    context = {"ppap_form": ppap_form}
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
        #     k.title = request.POST.get("title")
        #     k.content = request.POST.get("content")
        #     k.save()
        #     return redirect("/")

        # else:
        #     context = {"c": k}
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
