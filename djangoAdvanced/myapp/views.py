from django.shortcuts import render
import requests

# Create your views here.

def Home(request):
    return render(request, "index.html")

def Register(request):
    return render(request, "register.html")