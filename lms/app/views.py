from django.shortcuts import render,redirect
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
    institute = Institute.objects.filter(status='Active')
    testimonials = Testimonials.objects.all().order_by('-id')
    brands = Partners.objects.all().order_by('-id')
    return render(request, 'app/home.html', {'category':category, 'home_course':home_course, 'institute':institute, 'testimonials':testimonials,'brands':brands})

def search(request):
    query = request.GET['query']
    institute = Institute.objects.filter(status='Active')
    course = Courses.objects.filter(title__icontains = query)
    category = Categories.get_all_categories(Categories)
    return render(request, 'search/search.html', {'course': course, 'category':category,'institute':institute})
    

def contact(request):
    institute = Institute.objects.filter(status='Active')
    category = Categories.get_all_categories(Categories)
    return render(request, 'app/contact.html', {'category':category,'institute':institute})

def about(request):
    institute = Institute.objects.filter(status='Active')
    category = Categories.get_all_categories(Categories)
    return render(request, 'app/about.html', {'category':category,'institute':institute})


def courses(request):
        category = Categories.get_all_categories(Categories)
        institute = Institute.objects.filter(status='Active')
        courses = Courses.objects.all().order_by('-id')
        level = Level.objects.all()
        # if request.User:
        return render(request, 'app/courses.html', {'category':category,'courses':courses, 'level':level,'institute':institute})
        # else:
            # return redirect('register')
            
def filter_data(request):
    categories = request.GET.getlist('category[]')
    levels = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    print(price)
    if categories:
        course = Courses.objects.filter(category__id__in = categories).order_by('-id')
        
    elif levels:
        course = Courses.objects.filter(level__id__in = levels).order_by('-id')
    else:
        course = Courses.objects.all().order_by('id')
    t = render_to_string('app/ajaxcourse.html',{'course':course})
    return JsonResponse({'data':t})

@login_required
def coursedetail(request, slug):
    institute = Institute.objects.filter(status='Active')
    time_duration = video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))
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
    return render(request, 'app/course-detail.html', {'category':category, 'course':course,'course_id':course_id,'time_duration':time_duration, 'check_enroll': check_enroll,'institute':institute})
        
            

def experts(request):
    institute = Institute.objects.filter(status='Active')
    category =Categories.get_all_categories(Categories)
    return render(request, 'app/experts.html', {'category':category,'institute':institute})

def blog(request):
    institute = Institute.objects.filter(status='Active')
    return render(request, 'app/blog.html', {})

@login_required
def checkout(request, slug):
    institute = Institute.objects.filter(status='Active')
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
    return render(request, 'payment/checkout.html', {'category':category,'institute':institute})

@login_required    
def enrolled_courses(request):
    institute = Institute.objects.filter(status='Active')
    category = Categories.get_all_categories(Categories)
    course = Usercourse.objects.filter(user = request.user)
    return render(request, 'app/enrolled-courses.html', {'course':course, 'category':category,'institute':institute})
 
@login_required
def watchcourse(request, slug):
    institute = Institute.objects.filter(status='Active')
    course = Courses.objects.filter(slug=slug)
    lecture = request.GET.get('lecture')
    course_id = Courses.objects.get(slug=slug)
   
    try:
        check_enroll = Usercourse.objects.get(user=request.user, course=course_id)
        videos = video.objects.get(id=lecture)
        if course.exists():
            course = course.first()
        else:
            return redirect('notfound')
    except Usercourse.DoesNotExist:
        return redirect('notfound')    
    return render(request, 'app/course-watch.html',{'course':course,'videos':videos,'check_enroll':check_enroll, 'lecture':lecture,'institute':institute})

def notfound(request):
    institute = Institute.objects.filter(status='Active')
    category = Categories.get_all_categories(Categories)
    return render(request, 'base/error.html', {'category':category,'institute':institute})
       

def handler404(request,*args,**argv):
    institute = Institute.objects.filter(status='Active')
    category= Categories.get_all_categories(Categories)
    return render(request,'base/error.html',{'category':category,'institute':institute})