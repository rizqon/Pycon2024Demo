from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import TodoItem

# Create your views here.
def index(request):
    return render(request=request, template_name='base.html', context={'todo_items': TodoItem.objects.all()})


def add(request):
    content = request.POST.get('content', '')

    TodoItem.objects.create(content=content)
    
    return redirect('index')

def delete(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)

    todo.delete()

    return redirect('index')