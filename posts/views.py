from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Post
from .forms import PostModelForm

def home_view(request):
    posts = Post.objects.all()
    reverse_ordered_posts = Post.objects.order_by("-pub_date")
    context = {
        'posts': reverse_ordered_posts
        }
    return render(request, 'posts/home.html', context=context)

def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", { "post": post })

@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        raise PermissionDenied()
    if request.method == "POST":
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/{pk}/")
    else:
        form = PostModelForm(instance=post)
    return render(request, "posts/post_update.html", { "form": form, "post": post })

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            post = Post.objects.create(author=request.user, title=title, content=content)
            post.save()
            return redirect("/")
    else:
        form = PostModelForm()
    return render(request, "posts/create_post.html", {'form': form})

def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        raise PermissionDenied()
    if request.method == "POST":
        post.delete()
        return redirect("/")
    return render(request, "posts/delete_post.html", { "post":post })