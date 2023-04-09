from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'app/home.html', {})

def handler404(request,*args,**argv):
    return render(request,'base/error.html')