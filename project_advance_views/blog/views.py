from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm
# Create your views here.

def input_blog(request) :
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blog':blog})

def new_blog(request) :
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('new_blog')
    else:
        form = PostForm()
    return render(request, 'blog/new_blog.html', {'form': form})