from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from app.models import * 


def home(request):
    category = Categories.objects.all()
    home_course = Courses.objects.filter(status='PUBLISH').order_by('-id')
    return render(request, 'app/home.html', {'category':category, 'home_course':home_course})

def contact(request):
    return render(request, 'app/contact.html', {})

def about(request):
    return render(request, 'app/about.html', {})

class courses(View):
    def get(self, request):
        category = Categories.get_all_categories(Categories)
        c_courses = Courses.objects.all().order_by('-id')
        return render(request, 'app/courses.html', {'category':category,'c_courses':c_courses})

    

def experts(request):
    return render(request, 'app/experts.html', {})

def blog(request):
    return render(request, 'app/blog.html', {})
    

def handler404(request,*args,**argv):
    return render(request,'base/error.html')