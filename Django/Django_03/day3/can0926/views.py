from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
# 1번
def is_odd_even(request, n1):
    number = n1

    if number == 0:
        check = 0
    else:
        if number % 2:
            check = "홀수"
        else:
            check = "짝수"
    context = {
        "num": number,
        "check": check,
    }
    return render(request, "is_odd_even.html", context)


# 2번
def calculator(request, var1, var2):

    if var2 == 0:
        return render(request, "error.html")

    res_sum = var1 + var2
    res_sub = var1 - var2
    res_mul = var1 * var2
    res_div = var1 // var2

    context = {
        "sum": res_sum,
        "sub": res_sub,
        "mul": res_mul,
        "div": res_div,
        "var1": var1,
        "var2": var2,
    }

    return render(request, "calculator.html", context)


# 3번
def life_ago(request):
    return render(request, "life_ago.html")


def life_ago_show(request):
    name_ = request.GET.get("name_")
    prevs = [
        "왕",
        "노비",
        "대장금",
        "대장장",
        "신하",
    ]

    prev = random.choice(prevs)
    context = {"name_": name_, "before": prev}
    return render(request, "life_ago_show.html", context)


# 4번
def lorem_(request):
    return render(request, "lorem_.html")


def lorem_show(request):
    para_ = int(request.GET.get("para"))
    words_ = int(request.GET.get("words"))

    lorem_cnt = [[] for _ in range(para_)]
    words_cnt = [
        "사과",
        "바나나",
        "딸기",
        "정국",
        "제이홉",
        "RM",
        "진",
        "지민",
        "뷔",
        "슈가",
    ]

    for i in range(len(lorem_cnt)):
        while len(lorem_cnt[i]) < words_:
            word = random.choice(words_cnt)
            lorem_cnt[i].append(word)

    context = {"lorem_cnt": lorem_cnt}
    return render(request, "lorem_show.html", context)
