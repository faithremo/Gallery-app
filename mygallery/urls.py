from django.urls import path, re_path
from . import views

urlpatterns=[
    # path('',views.welcome,name = 'welcome'),
    path('',views.gallery, name='gallery'),
    path('today/',views.mygallery_of_day,name='galleryToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_mygallery, name= 'pastPhotos'),
    path('photo/<str:pk>', views.viewphoto, name='photo'),
    path('add/', views.addphoto, name='add'),
    
]



