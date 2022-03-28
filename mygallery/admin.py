from django.contrib import admin
from .models import mygallery

# Register your models here.

from .models import Photo, Category
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(mygallery)