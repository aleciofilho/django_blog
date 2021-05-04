from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from .models import Post
from .forms import PostForm

def home_view(request):
    posts = Post.objects.all()
    reverse_ordered_posts = Post.objects.order_by("-pub_date")
    context = {
        'posts': reverse_ordered_posts
        }
    return render(request, 'posts/home.html', context=context)

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/success/")
    else:
        form = PostForm()
    return render(request, "posts/create_post.html", {'form': form})