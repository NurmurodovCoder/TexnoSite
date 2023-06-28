from django.shortcuts import render, redirect
from .forms import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def signup(request):
    form = CustomUser()
    context = {"form": form}
    if request.method == "POST":
        form = CustomUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Royhatdan muvaffaqiyatli o`tdingiz")
            return redirect("post")

        else:
            messages.error(request, "Royhatdan o`tolmadingiz. Qandaudir xatolik bor!")
    return render(request, "users/signup.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz")
            return redirect("post")
        else:
            messages.error(request, "Xatolik bor. Qayta tekshiring !!!")
    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz !")
    return redirect("post")
