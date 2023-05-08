from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.
class Institute(models.Model):
    STATUS=(
        ('Active','Active'),
        ('Draft','Draft'),
    )
    name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='media/institute/logos', default=None, blank=True)
    address = models.CharField(max_length=500, null=False)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    portal_name = models.CharField(max_length=100)
    sub_text = models.CharField(max_length=200, default=None)
    status = models.CharField(choices= STATUS, max_length=100, null=True)
    
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
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices= STATUS, max_length=100, null=True)
    certificate = models.CharField(choices=CERT_STATUS, max_length=100, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("coursedetail", kwargs={'slug': self.slug})
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Courses.objects.filter(slug=slug).order_by('-id')
    exists =qs.exists()
    if exists:
        new_slug = "%s-%S" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug= create_slug(instance)
        
pre_save.connect(pre_save_post_reciever, Courses)
    
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
    description = models.TextField(null=True, default=None)
    time_duration = models.FloatField()
    preview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Usercourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    paid = models.BooleanField(default=0)
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ["user","course"]
    
    def __str__(self):
        return self.user.first_name +" - " +self.course.title
    
    
class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    testi_photo = models.ImageField(upload_to='media/testimonials', default=None)
    description = models.TextField(null=True, default=None)
    designation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Partners(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/partners')
    
    def __str__(self):
        return self.name

class News_Notices(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=True)
    documents = models.FileField(upload_to='media/News_Notices/documents', blank=True)
    
    def __str__(self):
        return self.title

class Upcoming_Events(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='media/events/upcoming',blank=True)
    def __str__(self):
        return self.title
        