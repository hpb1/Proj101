from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginhpg(request):
    return render(request, 'loginhpg.html')

def regis(request):
    return render(request, 'register.html')

def forpw(request):
    return render(request, 'forpw.html')

def forpw2(request):
    return render(request, 'forpw2.html')