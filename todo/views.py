from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, Item
from django.shortcuts import get_object_or_404
from .forms import TodoForm

# Create your views here.


def index(request):
    todo_list = Todo.objects.all()

    form = TodoForm(request.POST)

    if form.is_valid():
        title = form.cleaned_data['title']
        todo_items = form.cleaned_data['todo_items']
        all_items = todo_items.split(';')

        todo = Todo.objects.create(title=title)

        for item in all_items:
            Item.objects.create(content=item, todo=todo)

        redirect('index')

    content = {
        'todo_list': todo_list,
        'form': form,
    }

    return render(request, '../templates/pages/index.html', content)


def delete_item(request):
    item_uuid = request.GET.get('item_uuid')

    if(item_uuid):
        item = get_object_or_404(Item, uuid=item_uuid)
        item.delete()

    return redirect('index')


def delete_todo(request):
    todo_uuid = request.GET.get('todo_uuid')

    if(todo_uuid):
        todo = get_object_or_404(Todo, uuid=todo_uuid)
        todo.delete()

    return redirect('index')


def check_item(request):
    item_uuid = request.GET.get('item_uuid')

    if(item_uuid):
        item = get_object_or_404(Item, uuid=item_uuid)
        item.checked = not item.checked
        item.save()

    return redirect('index')
