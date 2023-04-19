from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from app.models import * 

def base(request):
    base_category = Categories.objects.all()
    return render(request, 'app/home.html', {base_category:'base_category'})
    

def home(request):
    category = Categories.objects.all()
    home_course = Courses.objects.filter(status='PUBLISH').order_by('-id')
    return render(request, 'app/home.html', {category:'category', home_course:'home_course'})

def contact(request):
    return render(request, 'app/contact.html', {})

def about(request):
    return render(request, 'app/about.html', {})

def courses(request):
    category = Categories.get_all_categories(Categories)
    return render(request, 'app/courses.html', {category:'category'})

def experts(request):
    return render(request, 'app/experts.html', {})

def blog(request):
    return render(request, 'app/blog.html', {})
    

def handler404(request,*args,**argv):
    return render(request,'base/error.html')