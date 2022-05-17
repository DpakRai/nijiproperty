from django import forms
from .models import NijiUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class NijiUserCreationForm(UserCreationForm):

   class Meta(UserCreationForm):
        model = NijiUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture')


class NijiUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = NijiUser
        fields = ('email', 'profile_picture')