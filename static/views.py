from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Blog.objects # Query set
    return render(request, "home.html", {"blogs": blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, "detail.html", {"blog":blog})

def write(request):
    return render(request, "write.html")

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str((blog.id)))