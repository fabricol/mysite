# blog/views.py

from django.shortcuts import render
from .models import Post

def home(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})