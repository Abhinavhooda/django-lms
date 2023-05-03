from django.urls import path,re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/contact', views.contact, name= 'contact'),
    path('app/about', views.about, name='about'),
    path('app/courses', views.courses.as_view(), name='courses'),
    path('course/<slug>', views.coursedetail.as_view(), name='coursedetail'),
    path('app/experts', views.experts, name='experts'),
    path('app/blog', views.blog, name='blog'),
    path('course/filter-data',views.filter_data,name="filter-data"),
    path('search', views.search, name='search'),
    path('checkout/<slug>', views.checkout, name='checkout'),
    path('enrolled_courses', views.enrolled_courses, name='enrolled_courses'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
handler404= 'app.views.handler404'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)