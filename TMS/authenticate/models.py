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


