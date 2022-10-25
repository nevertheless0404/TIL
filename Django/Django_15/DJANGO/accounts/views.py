from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import User
from .forms import UsersForm, kkUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def home(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/home.html", context)


def signup(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:home")
    else:
        form = UsersForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "accounts:home")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:home")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user1": user,
    }
    return render(request, "accounts/detail.html", context)


def update(request):
    if request.method == "POST":
        form = kkUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = kkUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("accounts:home")


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts:home")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


def follow(request, pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=pk)
        if request.user == person:
            messages.warning(request, "스스로 팔로우를 할 수 없습니다.")
            return redirect("accounts:detail", pk)
            # if request.user.followings.filter(pk=user_pk).exists():
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)

    return redirect("accounts:login")
