from django.contrib.auth.models import User
from django.db import models
from autoslug import *

# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=500, null=False)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    portal_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return self.name
    
    def get_all_categories(self):
        return Categories.objects.all().order_by('-id')
    
class Level(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    author_profile = models.ImageField(upload_to="media/author")
    name = models.CharField(null=True, max_length=50, default=None)
    author_role = models.CharField(null = True, max_length=200, default=None)
    about_author = models.TextField()
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    STATUS=(
        ('PUBLISH','PUBLISH'),
        ('DRAFT','DRAFT'),
    )
    CERT_STATUS=(
        ('Yes','yes'),
        ('No','no'),
    )
    featured_image = models.ImageField(upload_to="media/featured_img", null=True)
    featured_video = models.CharField(null=True, max_length=100)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(null=True, default=0)
    discount = models.IntegerField(null=True)
    language = models.CharField(null=True, default=None, max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, default=None, blank=False, null=True)
    status = models.CharField(choices= STATUS, max_length=100, null=True)
    certificate = models.CharField(choices=CERT_STATUS, max_length=100, null=True)
    
    def __str__(self):
        return self.title
    
class learning_point(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)
    points = models.CharField(max_length = 500, default=None)
    
    def __str__(self):
        return self.points
    
class requirement_point(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)
    points = models.CharField(max_length = 500, default=None)
    
    def __str__(self):
        return self.points
    
class lessons(models.Model):
    course=models.ForeignKey(Courses, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " - " + self.course.title
    
class video(models.Model):
    serial_number= models.IntegerField(null=True)
    thumbnail=models.ImageField(upload_to='media/course/lessons', height_field=None, width_field=None, max_length=None, null=True)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    lesson = models.ForeignKey(lessons, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    time_duration = models.IntegerField(null=True)
    preview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Usercourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    paid = models.BooleanField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name +" - " +self.course.title