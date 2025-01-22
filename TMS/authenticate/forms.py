from django import forms
from .models import UserProfileImage

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileImage
        fields = ['photo']

