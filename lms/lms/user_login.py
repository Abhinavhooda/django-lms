from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.EmailBackEnd import *

def Register(request):
    if request.method=="POST":
        username = request.POST.get('Username')
        email = request.POST.get("email")
        Password = request.POST.get("Password")

 # check email
        if User.objects.filter(email=email).exists():
           messages.warning(request,'Email are Already Exists !')
           return redirect('register')

 # check username
        if User.objects.filter(username=username).exists():
           messages.warning(request,'Username are Already exists !')
           return redirect('register')
        
        user = User(
            username=username,
            email=email,
            )
        user.set_password(Password)
        user.save()
        return redirect('login')

    return render(request, 'registration/register.html', {})
    
def Dologin(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("Password")
        user = EmailBackEnd.authenticate(request,username=email,password=password)
        if user!=None:
           login(request,user)
           return redirect('home')
        else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('login')
		   
def Profile(request):
    return render(request, 'registration/profile.html', {})
    