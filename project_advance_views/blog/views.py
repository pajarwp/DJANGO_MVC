from django.shortcuts import render
from .models import Blog
from .forms import PostForm
# Create your views here.

def input_blog(request) :
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blog':blog})
