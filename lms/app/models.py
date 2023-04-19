from django.db import models
from autoslug import *

# Create your models here.
class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return self.name
    
    def get_all_categories(self):
        return Categories.objects.all().order_by('-id')
    
class Level(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, default=None, blank=False, null=True)
    
    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    author_profile = models.ImageField(upload_to="media/author")
    name = models.CharField(null=True, max_length=50, default=None)
    about_author = models.TextField()
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    STATUS=(
        ('PUBLISH','PUBLISH'),
        ('DRAFT','DRAFT'),
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
    slug = AutoSlugField(populate_from='title', unique=True, default=None, blank=False, null=True)
    status = models.CharField(choices= STATUS, max_length=100, null=True)
    
    def __str__(self):
        return self.title
    