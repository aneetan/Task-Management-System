from django.shortcuts import render, redirect
from .models import GeneralUser, Project, ProjectUserRole
from .forms import UserProfileForm
from django.contrib.auth import login, authenticate, logout
from allauth.socialaccount.models import SocialAccount

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer, ProjectUserRoleSerializer

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

# Method to render the profile picture
def user_profile(userId):
    user = GeneralUser.objects.get(id = userId)
    profile = user.profile_pic
    print(profile)

    if profile:
        profile_image_url = 'http://127.0.0.1:8000/media/' + profile.photo.name
    else:
        profile_image_url = None
    
    return profile_image_url

def signup(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def upload_profile(request):
    return render(request, 'upload_profile.html')

#login/signup using google account
def home(request):
    if request.user.is_authenticated:
            social_account = SocialAccount.objects.get(user=request.user, provider='google')
            profile_image_url = social_account.extra_data.get('picture')
            context = {'user': request.user.username, 'profile' : profile_image_url}
            return render(request, 'index.html', context)

# signup using GeneralUser model
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

# login using generalUser model

@csrf_exempt 
def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            # Get or create a token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            
            profile = user_profile(user.id)
            return render(request, 'index.html', {'user': user, 'profile': profile})
        
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})


# upload user profile 
def user_profile_upload(request):
    if request.method == 'POST' and request.FILES['photo']:
        form = UserProfileForm(request.POST, request.FILES)
        id = request.session['id']                              #retrieve id from session
        user = GeneralUser.objects.get(id=id)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.userId = GeneralUser.objects.get(id=id)    #retrive user from id
            
            user_profile.save()

            user.profile_pic = user_profile
            user.save()

            return render(request, 'login.html')
    else:
        return render(request, 'user_profile.html')


#logout function
def logout_view(request):
    logout(request)
    return redirect("login")

#api to create a project
class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data 
        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():

            project = serializer.save()
            project.created_by.add(request.user) 

            ProjectUserRole.objects.create(role='admin', user = request.user, project = project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#api to invite user 
class ProjectUserInviteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data 
        serializer = ProjectUserRoleSerializer(data=data)
        if serializer.is_valid():
            project_id = serializer.validated_data['project'].projectId 

            is_admin = ProjectUserRole.objects.filter(
                project_id = project_id, user=request.user, role="admin"
            ).exists()

            if not is_admin:
                return Response({'error': 'You cannot invite users'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
