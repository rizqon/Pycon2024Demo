from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import TodoItem
from auth.decorators.authenticated import authenticated
from asgiref.sync import sync_to_async

# Create your views here.
@authenticated(fetch_user_info=True)
@sync_to_async
def index(request):
    return render(request=request, template_name='base.html', context={'todo_items': TodoItem.objects.all(), 'user': request.user_info})


@authenticated()
@sync_to_async
def add(request):
    content = request.POST.get('content', '')

    TodoItem.objects.create(content=content)
    
    return redirect('index')

@authenticated()
@sync_to_async
def delete(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)

    todo.delete()

    return redirect('index')