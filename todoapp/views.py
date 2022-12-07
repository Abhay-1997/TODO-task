from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    if request.method == 'POST':
        task = request.POST['task']
        obj = Task(task=task,)
        obj.save()
        return HttpResponseRedirect(reverse('all'))
    return render(request, 'Add task.html')


def update(request, pk):
    if request.method == 'POST':
        status = request.POST['status']
        obj = Task.objects.get(id=pk)
        obj.status = status
        obj.save()
        return HttpResponseRedirect(reverse('all'))
    obj = Task.objects.get(id=pk)
    return render(request, 'update.html', {'obj': obj})


def all(request):
    objs = Task.objects.all()
    return render(request, 'All tasks.html', {'objs': objs})


def complete(request):
    objs = Task.objects.filter(status='Completed')
    return render(request, 'complete.html', {'objs': objs})


def pending(request):
    objs = Task.objects.filter(status='Pending')
    return render(request, 'pending.html', {'objs': objs})


def delete(request, pk):
    obj = Task.objects.get(id=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('all'))
