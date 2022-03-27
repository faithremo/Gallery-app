from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharFiled(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharFiled(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.name
