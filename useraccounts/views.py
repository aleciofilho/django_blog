from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, "useraccounts/login.html", { "form":form })

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            user = User.objects.create(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "useraccounts/register.html", { "form":form })

def profile_view(request, username):
    qs = User.objects.filter(username__iexact=username)
    if qs.exists() and qs.count() == 1:
        user = qs.first()
    return render(request, "useraccounts/profile.html", {"user": user})