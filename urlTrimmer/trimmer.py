from django import forms
from django.shortcuts import render

def index(request):
    form = forms.CharField(label="Best",max_length=164)
    return render(request,"../templates/mainForm.html",{"form":form})