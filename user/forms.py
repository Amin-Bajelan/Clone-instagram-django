from django import forms
from .models import UserProfile, Post


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        labels = {'Please enter your username:': 'Username',
                  'Please enter your email:': 'Email', 'set password:': 'Password'}


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['password', 'bio', 'profile_picture', 'is_private']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
