from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm, ProfileUpdateModelForm, UserUpdateModelForm
from posts.models import Post

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
    # qs = User.objects.filter(username__iexact=username)
    # if qs.exists() and qs.count() == 1:
    #     user = qs.first()
    user = get_object_or_404(User, username=username)
    latest_posts = Post.objects.filter(author__exact=user).order_by("-pub_date")[:5]

    context = {
        "user": user,
        "posts": latest_posts
    }
    return render(request, "useraccounts/profile.html", context)

def profile_settings_view(request):
    user = request.user
    user_form = UserUpdateModelForm(instance=user, request=request)
    profile_form = ProfileUpdateModelForm(instance=user.profile)

    if request.method == "POST":
        user_form = UserUpdateModelForm(request.POST, request=request, instance=user)
        profile_form = ProfileUpdateModelForm(request.POST, request.FILES, instance=user.profile)
        print(user_form.is_valid())
        print(profile_form.is_valid())
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("/profile/settings/")
    
    user_form = UserUpdateModelForm(instance=user, request=request)
    profile_form = ProfileUpdateModelForm(instance=user.profile)
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "useraccounts/profile_settings.html", context)