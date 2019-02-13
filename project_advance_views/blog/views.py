from django.shortcuts import render, redirect, get_list_or_404
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
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog/new_blog.html', {'form': form})

def post_detail(request, post_id):
    post_num = get_list_or_404(Blog, id=post_id)
    return render(request, 'blog/blog_num.html', {'blog': post_num})