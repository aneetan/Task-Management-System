from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('upload_profile/', views.upload_profile, name='upload_profile'),
    path('process_signup/', views.process_signup, name='process_signup'),
    path('process_login/', views.process_login, name='process_login'),

]
