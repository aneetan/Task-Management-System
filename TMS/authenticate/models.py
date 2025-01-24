from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class GeneralUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserProfileImage(models.Model):
    profileId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return f"{self.userId.name}'s Profile"

class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectUserRole(models.Model):
    ROLE_CHOICES= [
        ('Admin', 'Admin'),
        ('Team Member', 'Team Member')
    ]

    project_user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    project = models.ForeignKey(GeneralUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices= ROLE_CHOICES)

    def __str__(self):
        return self.role