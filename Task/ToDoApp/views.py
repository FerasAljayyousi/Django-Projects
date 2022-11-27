from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import todo
def list_todo_items(request):
    context = {'todo_list' : todo.objects.all()}
    return render(request,'index.html', context)

def insert(request:HttpRequest):
    TODO = todo(create = request.POST['create'])
    TODO.save()
    return redirect('list_todo_items')

def delete(request, to_id):
    delete_item = todo.objects.get(id= to_id)
    delete_item.delete()
    return redirect("list_todo_items")
# Create your views here.
