from django.db import models

# Create your models here.
class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, default=None)
    
    def __str__(self):
        return self.name
    