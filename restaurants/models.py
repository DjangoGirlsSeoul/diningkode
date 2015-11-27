from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    # ...
    # code here
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

    def __str__(self):
        return self.name

