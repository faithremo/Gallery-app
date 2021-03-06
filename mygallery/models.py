from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    #image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.description

#class mygallery(models.Model):
    #title field
    #title = models.CharField(max_length=100)
    #image field
    #image = CloudinaryField('image')