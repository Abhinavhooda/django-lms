from django.contrib import admin
from .models import * 

# Register your models here.
class learning_points_tublarinline(admin.TabularInline):
    model=learning_point
class requirement_tublerinline(admin.TabularInline):
    model=requirement_point
    
class video_tublerinline(admin.TabularInline):
    model=video
    
class course_fields(admin.ModelAdmin):
    inlines=(learning_points_tublarinline, requirement_tublerinline, video_tublerinline)
    
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Courses, course_fields)
admin.site.register(Level)
admin.site.register(Institute)
# admin.site.register(learning_point)
# admin.site.register(requirement_point)
admin.site.register(lessons)
admin.site.register(video)
admin.site.register(Usercourse)
admin.site.register(Testimonials)
admin.site.register(Partners)
admin.site.register(Upcoming_Events)
admin.site.register(News_Notices)