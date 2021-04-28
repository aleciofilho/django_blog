from django.shortcuts import render

# Create your views here.

from .models import Post

def home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
        }
    return render(request, 'posts/home.html', context=context)