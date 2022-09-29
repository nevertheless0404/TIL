from multiprocessing import context
from django.shortcuts import render, redirect

import todos
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def detail(request, pk_):
    todos = Todo.objects.get(id=pk_)
    context = {
        "todos": todos,
    }

    return render(request, "todos/detail.html", context)


def edit(request, pk_):
    todos = Todo.objects.get(id=pk_)
    k = request.GET
    v = [k[i] for i in k]
    context = {
        "todos": todos,
        "c": v,
    }

    return render(request, "todos/edit.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }
    return redirect("todos:index")


def update(request, pk_):
    hello = Todo.objects.get(id=pk_)
    content_ = request.GET.get("content")
    priority_ = request.GET.get("priority")
    deadline_ = request.GET.get("dealine")

    hello.content = content_
    hello.priority = priority_
    hello.deadline = deadline_

    hello.save()
    return redirect("todos:edit", hello.pk)


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todos:index")
