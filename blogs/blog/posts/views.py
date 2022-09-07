from django.shortcuts import render
from .models import post

def index(request):
    posts = post.objects.all()
    return render(request, 'index.html',{'posts':posts})

def postt(request,pk):
    posts = post.objects.get(id=pk)
    return render(request, 'post.html', {'posts':posts})


# Create your views here.
