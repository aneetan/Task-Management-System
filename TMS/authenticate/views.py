from django.shortcuts import render
from .models import GeneralUser

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def upload_profile(request):
    return render(request, 'upload_profile.html')

def process_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        generalUser = GeneralUser(name=name, email=email, phone=phone, password=password)
        generalUser.save()

        return render(request, 'upload_profile.html')
    else:
        return render(request, 'signup.html')
    
def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = GeneralUser.objects.get(email=email)
        if (password == user.password):
            request.session['email'] = user.email

            return render(request, 'index.html', {user:user})
        
        else:
            return render(request, 'login.html')

        

    
