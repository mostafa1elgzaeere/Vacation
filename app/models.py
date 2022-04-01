from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,AbstractUser


class Vacation(Model):
    employee=ForeignKey('CustomUser',on_delete=CASCADE,unique=True)
    start_at=DateField()
    end_at=DateField()
    reason=CharField(max_length=200)
    
    def __str__(self):
        return f"{self.employee} take a vication from {self.start_at} to {self.end_at} "
    
    
class CustomUser(AbstractUser):
    mobile_number=IntegerField(max_length=25)
    
    def __str__(self):
        return f"{self.username}"
    
    

    
'''
    User
        - first name
        - last name 
        - email
    
    
    CustomUser 
        User
        mobile_number   

'''
