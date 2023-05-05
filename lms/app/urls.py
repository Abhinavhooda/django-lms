from django.urls import path,re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from app import views

urlpatterns = [
#------------homepage
    path('', views.home, name='home'),
#------------app views
    path('app/contact', views.contact, name= 'contact'),
    path('app/about', views.about, name='about'),
    path('app/courses', views.courses, name='courses'),
    path('app/blog', views.blog, name='blog'),
    path('app/experts', views.experts, name='experts'),
#------------search
    path('search', views.search, name='search'),
#------------Coursedetail, filter & watch
    path('course/<slug:slug>', views.coursedetail, name='coursedetail'),
    # path('course/filter-data',views.filter_data,name='filter-data'),
    path('course/watch/$=<slug:slug>', views.watchcourse, name='watchcourse'),
#------------Checkout & Enroll
    path('checkout/<slug>', views.checkout, name='checkout'),
    path('enrolled_courses', views.enrolled_courses, name='enrolled_courses'),
#------------Errors
    path('notfound', views.notfound, name='notfound')
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
handler404= 'app.views.handler404'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)