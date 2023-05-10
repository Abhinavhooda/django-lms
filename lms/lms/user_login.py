from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app.EmailBackEnd import *
from app.models import *

def Register(request):
    institute = Institute.objects.filter(status='Active')
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
    return render(request, 'registration/register.html',{'institute':institute})
    
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
    institute = Institute.objects.filter(status='Active')
    return render(request, 'registration/profile.html', {'institute':institute})

def Profile_update(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile successfully updated. ')
        return redirect('profile')
    
    