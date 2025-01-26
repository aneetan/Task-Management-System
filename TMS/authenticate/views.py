from django.shortcuts import render
from .models import GeneralUser, UserProfileImage
from .forms import UserProfileForm
from django.contrib.auth import login, authenticate

# Create your views here.
def user_profile(userId):
    user = GeneralUser.objects.get(id = userId)
    profile = user.profile_pic

    if profile:
        profile_image_url = profile.photo
    else:
        profile_image_url = None
    
    return profile_image_url

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def upload_profile(request):
    return render(request, 'upload_profile.html')

def process_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        generalUser = GeneralUser(username=name, email=email, phone=phone)
        generalUser.set_password(password)
        generalUser.save()

        user = GeneralUser.objects.get(email=email)
        request.session['id'] = user.id

        return render(request, 'upload_profile.html')
    else:
        return render(request, 'signup.html')
    
def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user1 = GeneralUser.objects.get(email=email)
        profile = user_profile(user1.id)

        user = authenticate(request, username = email, password=password)
        
        if user is not None:
            request.session['id'] = user.id
            return render(request, 'index.html', {'user': user, 'profile': profile})
        
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

def user_profile_upload(request):
    if request.method == 'POST' and request.FILES['photo']:
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            id = request.session['id']                              #retrieve id from session
            user_profile.userId = GeneralUser.objects.get(id=id)    #retrive user from id
            
            user_profile.save()

            return render(request, 'login.html')
    else:
        return render(request, 'user_profile.html')




    
