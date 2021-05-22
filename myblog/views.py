from django.shortcuts import render
from .models import Posts

# Create your views here.


def home(request):
    posts = {'posts': Posts.objects.all()}
    return render(request, 'myblog/home.html', posts)


def about(request):
    return render(request, 'myblog/about.html', {'title': 'About'})
