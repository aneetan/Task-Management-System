from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class GeneralUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    profile_pic = models.OneToOneField(
        'UserProfileImage',
        on_delete=models.SET_NULL,
        null=True
    )

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class UserProfileImage(models.Model):
    profileId = models.AutoField(primary_key=True)
    userId = models.OneToOneField(
        GeneralUser,
        on_delete=models.CASCADE,
        related_name='profile_image'
    )
    photo = models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return f"{self.userId.username}'s Profile"

class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ManyToManyField(GeneralUser, related_name= 'project_creator')
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_roles')
    role = models.CharField(max_length=20, choices= ROLE_CHOICES)

    def __str__(self):
        return self.role