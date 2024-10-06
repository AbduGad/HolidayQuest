# models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Using the ORM in views or other parts of the app:
# 1. Creating a new record
hotel = Hotel(name="Sunset Hotel", city="New York", rating=5)
hotel.save()

# 2. Querying the database
all_hotels = Hotel.objects.all()
ny_hotels = Hotel.objects.filter(city="New York")
top_hotels = Hotel.objects.filter(rating__gte=4)
