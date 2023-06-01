from django.http import Http404
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_dateil(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No post")
    return render(request, 'blog/post/detail.html', {'post': post})
