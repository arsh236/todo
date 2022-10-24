from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from task.models import Task

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control border border-info'}),
            'password': forms.PasswordInput(attrs={'class':'form-control border border-info'})
           
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border  border-warning','PlaceHolder':'enter username' }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border  border-warning','PlaceHolder':'enter password'}))


class TaskUpadateForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task_name','status']


