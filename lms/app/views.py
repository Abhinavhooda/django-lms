from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from app.models import * 
from django.template.loader import render_to_string
from django.db.models import Sum
from django.http import JsonResponse


def home(request):
    category = Categories.get_all_categories(Categories)
    home_course = Courses.objects.filter(status='PUBLISH').order_by('-id')
    time_duration = video.objects.filter().aggregate(sum=Sum('time_duration'))
    return render(request, 'app/home.html', {'category':category, 'home_course':home_course, 'time_duration':time_duration})

def search(request):
    query = request.GET['query']
    course = Courses.objects.filter(title__icontains = query)
    category = Categories.get_all_categories(Categories)
    return render(request, 'search/search.html', {'course': course, 'category':category})
    

def contact(request):
    category = Categories.get_all_categories(Categories)
    return render(request, 'app/contact.html', {'category':category})

def about(request):
    category = Categories.get_all_categories(Categories)
    return render(request, 'app/about.html', {'category':category})


def courses(request):
        category = Categories.get_all_categories(Categories)
        courses = Courses.objects.all().order_by('-id')
        level = Level.objects.all()
        # if request.User:
        return render(request, 'app/courses.html', {'category':category,'courses':courses, 'level':level})
        # else:
            # return redirect('register')

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    if price == ['pricefree']:
        course = Courses.objects.filter(price=0)
    elif price == ['pricepaid']:
        course = Courses.objects.filter(price__gte=1)
    elif price == ['priceall']:
        course = Courses.objects.all()
    elif category:
        course = Courses.objects.filter(category__id__in = category).order_by('-id')
    elif level:
        course = Courses.objects.filter(level__id__in = level).order_by('-id')
    else:
       course = Courses.objects.all().order_by('-id')
    t = render_to_string('ajax/course.html', {'course': course})
    return JsonResponse({'data': t})

@login_required
def coursedetail(request, slug):
        time_duration = video.objects.filter().aggregate(sum=Sum('time_duration'))
        category = Categories.get_all_categories(Categories)
        course = Courses.objects.filter(slug=slug)
        if course.exists():
            course=course.first()
        else:
            return redirect('notfound')
        course_id = Courses.objects.get(slug=slug)
        try:
            check_enroll=Usercourse.objects.get(user= request.user, course=course_id)
        except Usercourse.DoesNotExist:
            check_enroll=None
        return render(request, 'app/course-detail.html', {'category':category, 'course':course,'course_id':course_id,'time_duration':time_duration, 'check_enroll': check_enroll})
        
            

def experts(request):
    category =Categories.get_all_categories(Categories)
    return render(request, 'app/experts.html', {'category':category})

def blog(request):
    return render(request, 'app/blog.html', {})

@login_required
def checkout(request, slug):
    category = Categories.get_all_categories(Categories) 
    course=Courses.objects.get(slug=slug)    
    if course.discount == 100 :
        usercourse=Usercourse(
            user = request.user,
            course=course
        )
        usercourse.save()
        messages.success(request,'Courses successfully enrolled ! ')
        return redirect('enrolled_courses')
    return render(request, 'payment/checkout.html', {'category':category})

@login_required    
def enrolled_courses(request):
    category = Categories.get_all_categories(Categories)
    course = Usercourse.objects.filter(user = request.user)
    return render(request, 'app/enrolled-courses.html', {'course':course, 'category':category})
 
@login_required
def watchcourse(request, slug):
    lecture = request.GET.get('lecture')
    videos = video.objects.get(id=lecture)
    course_id = Courses.objects.get(slug=slug)
    course = Courses.objects.filter(slug=slug)

    try:
        check_enroll =Usercourse.objects.get(user=request.user, course=course_id)
        videos = video.objects.get(id=lecture)
        if course.exists():
            course = course.first()
        else:
            return redirect('notfound')
    except Usercourse.DoesNotExist:
        return redirect('notfound')    
    return render(request, 'app/course-watch.html',{'course':course,'videos':videos, 'check_enroll':check_enroll})

def notfound(request):
    category = Categories.get_all_categories(Categories)
    return render(request, 'base/error.html', {'category':category})
       

def handler404(request,*args,**argv):
    category= Categories.get_all_categories(Categories)
    return render(request,'base/error.html',{'category':category})