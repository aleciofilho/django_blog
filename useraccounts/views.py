from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import RegisterForm, LoginForm

# Create your views here.

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(form.errors.items())
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("success/")
    else:
        form = LoginForm()
    return render(request, "login.html", { "form":form })

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
            user.save()
            return redirect("success/")
    else:
        form = RegisterForm()
    return render(request, "register.html", { "form":form })

def profile_view(request, username):
    user = User.objects.filter(username__iexact=username)
    return render(request, "profile.html", {"user": user})