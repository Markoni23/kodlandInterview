from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "index.html"
