from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from .models import Category
# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    return render(request,'blog/blog_list.html',{'posts':posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'blog/blog_detail.html',{'post':post})

def post_details(request, category_slug, post_slug):
    category = get_object_or_404(Category,slug=category_slug)
    post = get_object_or_404(Post, slug=post_slug, category=category)
    return render(request, 'blog/post_details.html', {'post': post})