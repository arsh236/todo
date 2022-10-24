"""taskapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from task.views import AddTaskView, IndexView, LoginView,TaskListView,TaskDetailView,TaskDeleteView,LogView,RegistrationView,signout_view,TaskUpdateView

urlpatterns =[
    path('admin/', admin.site.urls),
    path('home/',IndexView.as_view()),
    path('login/',LoginView.as_view()),
    path('add_task/',AddTaskView.as_view(),name='todo-add'),
    path('add_task/all/',TaskListView.as_view(),name='todo-all'),
    path('task/<int:id>/',TaskDetailView.as_view(),name='todo-detail'),
    path('task/<int:id>/delete/',TaskDeleteView.as_view(),name='todo-delete'),
    path('register',RegistrationView.as_view(),name='todo-reg'),
    path('',LogView.as_view(),name='todo-log'),
    path('logout',signout_view,name='signout'),
    path('task/<int:id>/edit/',TaskUpdateView.as_view(),name='edit'),


]
