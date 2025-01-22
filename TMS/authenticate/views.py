from django.shortcuts import render
from .models import GeneralUser
from .forms import UserProfileForm
from django.contrib.auth.hashers import make_password, check_password

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

        generalUser = GeneralUser(name=name, email=email, phone=phone, password=make_password(password))
        generalUser.save()

        return render(request, 'upload_profile.html')
    else:
        return render(request, 'signup.html')
    
def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = GeneralUser.objects.get(email=email)
        if (check_password(password, user.password)):
            request.session['email'] = user.email
            request.session['id'] = user.id


            return render(request, 'index.html', {user:user})
        
        else:
            return render(request, 'login.html')

def user_profile_upload(request):
    if request.method == 'POST' and request.FILES['photo']:
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            # user_profile.userId = request.user
            
            user_profile.save()

            return render(request, 'index.html')
    else:
        return render(request, 'user_profile.html')



    
