from django.shortcuts import render,redirect
from .models import TodoModel
from .form import TodoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')
@login_required
def todolist(request):
    if request.method =='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save(commit=False).user=request.user
            form.save()
        messages.success(request,'Task added successfully !')
        return redirect('todolist')
    else: 
        tasks = TodoModel.objects.filter(user=request.user)
        paginator=Paginator(tasks,5)
        page=request.GET.get('pg')
        tasks=paginator.get_page(page)
        return render(request, 'todolist.html',{'tasks':tasks})
        
@login_required        
def delete_task(request,pk):
    task=TodoModel.objects.get(pk=pk) 
    if task.user==request.user:
        task.delete()
    else:
        messages.error(request,"Access Restricted!")
    return redirect('todolist')
@login_required
def edit_task(request,pk):
    task=TodoModel.objects.get(pk=pk)
    if request.method=='POST':
        form=TodoForm(instance=task,data=request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,"Task updated successfully")
    else:
        return render(request,'edit.html',{'task':task})
    return redirect('todolist')

@login_required
def completed_status(request,pk):
    task=TodoModel.objects.get(pk=pk)
    if task.user==request.user:
        task.status=True
        task.save()
    else:
        messages.error(request,"Access Restricted!")
    return redirect('todolist')

@login_required
def pending_status(request,pk):
    task=TodoModel.objects.get(pk=pk)    
    if task.user==request.user:
        task.status=False
        task.save()
    else:
        messages.error(request,"Access Restricted!")
    return redirect('todolist')


def contact(request):
    context={'contact':'Contact PAGE'}
    return render(request, 'contact.html',{'context':context})


def aboutus(request):
    context={'aboutus':'AboutUS PAGE'}
    return render(request, 'contact.html',context)
    
    