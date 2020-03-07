from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(response):
	return render(response, "main/home.html", {})

def profile(response):
	return render(response, "profile/profile.html", {})

def statements(response):
    return render(response, "statements/statements.html",{})