from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from app.models import * 
from django.template.loader import render_to_string
from django.db.models import Sum
from django.http import JsonResponse


def home(request):
    category = Categories.objects.all()
    home_course = Courses.objects.filter(status='PUBLISH').order_by('-id')
    return render(request, 'app/home.html', {'category':category, 'home_course':home_course})

def search(request):
    query = request.GET['query']
    course = Courses.objects.filter(title__icontains = query)
    return render(request, 'search/search.html', {'course': course})
    

def contact(request):
    return render(request, 'app/contact.html', {})

def about(request):
    return render(request, 'app/about.html', {})

class courses(View):
    def get(self, request):
        category = Categories.get_all_categories(Categories)
        courses = Courses.objects.all().order_by('-id')
        level = Level.objects.all()
        return render(request, 'app/courses.html', {'category':category,'courses':courses, 'level':level})

def filter_data(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')
    if category:
        course = Courses.objects.filter(category_id__in = category).order_by('-id')
    else:
        course = Courses.objects.all().order_by('id')
    # if price == ['pricefree']:
    #     course = Courses.objects.filter(price=0)
    # elif price == ['pricepaid']:
    #     course = Courses.objects.filter(price__gte=1)
    # elif price == ['priceall']:
    #     course = Courses.objects.all()
    # elif category:
    #     course = Courses.objects.filter(category__id__in = category).order_by('-id')
    # elif level:
    #     course = Courses.objects.filter(level__id__in = level).order_by('-id')
    # else:
    #    course = Courses.objects.all().order_by('-id')
    data = render_to_string('ajax/course.html', {'course': course})
    return JsonResponse({'data': data})

class coursedetail(View):
    def get (self, request, slug):
        time_duration = video.objects.filter().aggregate(sum=Sum('time_duration'))
        course = Courses.objects.get(slug=slug)
        course_id = Courses.objects.get(slug=slug)
        try:
            check_enroll=Usercourse.objects.get(user= request.user, course=course_id)
        except Usercourse.DoesNotExist:
            check_enroll=None
        course_object = Courses.objects.get(slug=slug)
        course_object.save()
        return render(request, 'app/course-detail.html', {'course':course,'course_id':course_id, 'time_duration':time_duration, 'check_enroll': check_enroll})
        
            

def experts(request):
    return render(request, 'app/experts.html', {})

def blog(request):
    return render(request, 'app/blog.html', {})

def checkout(request, slug):
    course=Courses.objects.get(slug=slug)
    if course.price == 0 :
        usercourse=Usercourse(
            user = request.user,
            course=course
        )
        usercourse.save()
        return redirect('courses')
    return render(request, 'payment/checkout.html', {})
    
def enrolled_courses(request):
    course = Usercourse.objects.filter(user = request.user)
    return render(request, 'app/enrolled-courses.html', {'course':course})
    

def handler404(request,*args,**argv):
    return render(request,'base/error.html')