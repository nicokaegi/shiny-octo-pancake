from django.shortcuts import render, redirect
from .models import ListItem
from .forms import ItemForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = ListItem.objects.all
            messages.success(request, ("added a new item to the list"))
            return render(request, 'home.html', {'list_items' : all_items})
    else:
        all_items = ListItem.objects.all
        return render(request, 'home.html', {'list_items' : all_items})

def about(request):
    return render(request, 'about.html',)

def delete(request, list_id):
    item = ListItem.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("item removed"))
    return redirect('home')


def complete(request, list_id):
    item = ListItem.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request, ("item completed"))
    return redirect('home')

def edit(request, list_id):
    if request.method == "POST":
        item = ListItem.objects.get(pk=list_id)
        form = ItemForm(request.POST or None, instance=item)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, ("item edited "))
            return redirect('home')
    else:
        item = ListItem.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item' : item})
