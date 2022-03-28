from re import template
from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Category, Photo

# Create your views here.
def welcome(request):
    return HttpResponse('My Gallery')


def mygallery_of_day(request):
    date = dt.date.today()
    return render(request, 'all-photos/todays-photos.html', {"date": date,})
    
  
def past_days_mygallery(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    if date == dt.date.today():
        return redirect(mygallery_of_day)

    return render(request, 'all-photos/past-photos.html', {"date": date})

    
    
def welcome(request):
    return render(request, 'welcome.html')


def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})

def addphoto(request):
    categories = Category.objects.all()
    
    context = {'categories': categories}
    return render(request, 'add.html', context)











