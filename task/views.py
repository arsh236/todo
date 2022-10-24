import imp
from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,UpdateView
from task.forms import LoginForm,RegistrationForm,TaskUpadateForm  
from task.models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'u must login')
            return redirect ('todo-log')
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')


class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

@method_decorator(signin_required,name='dispatch')
class AddTaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'addtask.html')
    
    def post(self,request,*args,**kwargs):
        uname=request.user
        tasks=request.POST.get('tasks')
        Task.objects.create(user=uname,task_name=tasks)
        messages.success(request,"task has been created")
        return redirect('todo-all')

@method_decorator(signin_required,name='dispatch')
class TaskListView(ListView):
    model= Task
    template_name='task_list.html'
    context_object_name='todos'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         qs=request.user.task_set.all()
    #       #  qs=Task.objects.filter(user=request.user)
    #         return render(request,'task_list.html',{'todos':qs})
    #     else:
    #         return redirect('todo-log')

#localhost:8000/details/{id}
@method_decorator(signin_required,name='dispatch')
class TaskDetailView(DetailView):
     model=Task
     template_name='task-details.html'
     context_object_name='todo'
     pk_url_kwarg='id'
    
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get('id')
    #     taskk=Task.objects.get(id=id)
    #     return render(request,'task-details.html',{'todo':taskk})

#localhost:8000/details/{id}/delete
@method_decorator(signin_required,name='dispatch')
class TaskDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        # tsk=Task.objects.get(id=id)
        # tsk.delete()
        Task.objects.filter(id-id).delete()
        messages.success(request,'task deleted')
        return redirect('todo-all')


class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'account created')
            return redirect("todo-log")
        else:
            messages.error(request,'registartion failed')
            return render(request,"registration.html",{"form":form})


class LogView(View):
    
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'log.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,'login success')
                return redirect('todo-all')
            else:
                messages.error(request,'invalid credentials')
                return render(request,'log.html',{"form":form})    
    

def signout_view(request,*args,**kwargs):
        logout(request)
        return redirect('todo-log')

class TaskUpdateView(UpdateView):
    model=Task
    form_class=TaskUpadateForm
    template_name='task_update.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('todo-all')