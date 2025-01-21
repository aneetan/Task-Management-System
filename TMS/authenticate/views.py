from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def upload_profile(request):
    return render(request, 'upload_profile.html')