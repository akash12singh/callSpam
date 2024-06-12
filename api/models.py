from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    likelihood = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Spam(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    likelihood = models.FloatField(default=0.0)  # Spam likelihood, ranging from 0 to 1

    def __str__(self):
        return self.phone_number
