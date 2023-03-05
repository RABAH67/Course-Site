from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil




class SingupForm(UserCreationForm):
    
    
    class Meta:
        
        model = User
        
        fields = ['username','email','password1','password1']
        
        
        
        
        
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['bio','addres']
