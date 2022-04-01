from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Vacation
from django.forms import *


class RegisterForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=["username","email","password","mobile_number"]
    
    
    
# class VacationForm(ModelForm):
#     class Meta:
#         model=Vacation
#         fields=["employee","start_at","end_at","reason"]
        
