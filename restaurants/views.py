from django.shortcuts import render
from django.http import Http404
from .models import Restaurant, Review

def list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/list.html', {"restaurants": restaurants})

def detail(request, name):
    # restaurant = ???
    # https://docs.djangoproject.com/en/1.8/topics/db/queries/#retrieving-a-single-object-with-get
    return render(request, 'restaurants/detail.html', {"restaurant": restaurant})

def rating(request, value):
    rating_value = float(value)
    # code here
    # https://docs.djangoproject.com/en/1.8/topics/db/queries/#retrieving-specific-objects-with-filters
    return render(request, 'restaurants/rating.html', {"restaurants": restaurants, "rating_value": rating_value})
