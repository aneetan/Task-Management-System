from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class GeneralUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    profileId = models.AutoField(primary_key=True)
    # userId = models.ForeignKey('GeneralUser', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return f"{self.userId.name}'s Profile"