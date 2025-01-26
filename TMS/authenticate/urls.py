from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('upload_profile/', views.upload_profile, name='upload_profile'),
    path('process_signup/', views.process_signup, name='process_signup'),
    path('process_login/', views.process_login, name='process_login'),
    path('user_profile_upload/', views.user_profile_upload, name='user_profile_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # settings.MEDIA_URL => specifies base url where media files are acessible
    # http://127.0.0.1:8000/media/filename
