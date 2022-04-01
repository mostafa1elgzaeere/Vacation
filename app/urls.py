from unicodedata import name
from django.contrib import admin
from django.urls import path

from app.views import Home,Signup

urlpatterns = [
    path("",Home,name="home"),
    path("accounts/signup/",Signup,name="account_signup"),
]
