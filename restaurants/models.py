from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    rating = models.FloatField()
    image = models.URLField()
    reviews = models.ForeignKey('Review')


class Review(models.Model):
    author = models.ForeignKey(User)
    review_text = models.TextField()
    rating = models.FloatField()
    
