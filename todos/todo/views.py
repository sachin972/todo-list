from multiprocessing.sharedctypes import Value
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Lists
from django import forms
from django.template import loader

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    description = forms.CharField(label = "Description")
    progress = forms.CharField(label="Progess")
    comments = forms.CharField(label="Comments")

# Create your views here.
def index(request):
    return render(request,"todo/index.html",{
        "todos" : Lists.objects.all()
    })

def todoList(request, todo_id):
    todo = Lists.objects.get(id = todo_id)
    return render(request,"todo/todo.html",{
        "todo" : todo
    })

def add(request):
    if(request.method == "POST"):
        form = NewTaskForm(request.POST)
        if(form.is_valid):
            todo = Lists()
            todo.todo = request.POST.get('task')
            todo.description = request.POST.get('description')
            todo.progress = request.POST.get('progress')
            todo.comments = request.POST.get('comments')
            todo.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,"todo/add",{
                "form" : form
            })
    else:
        return render(request,"todo/add.html",{
            "form":NewTaskForm()
        })


def update(request, todo_id):
    elem = Lists.objects.get(id = todo_id)
    template = loader.get_template('todo/update.html')
    context = {
        'element' : elem
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request, todo_id):\

    todo = request.POST['todo']
    description = request.POST['description']
    progress = request.POST['progress']
    comments = request.POST['comments']
    member = Lists.objects.get(id=todo_id)
    member.todo = todo
    member.description = description
    member.progress = progress
    member.comments = comments
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, todo_id):
    member = Lists.objects.get(id=todo_id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))