from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from app.models import * 

def home(request):
    category = Categories.objects.all()
    return render(request, 'app/home.html', {category:'category'})

def contact(request):
    return render(request, 'app/contact.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def courses(request):
    return render(request, 'app/courses.html', {})
    
    
    

def handler404(request,*args,**argv):
    return render(request,'base/error.html')