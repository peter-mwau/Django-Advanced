from django.shortcuts import render
import requests
import json
# from django.contrib.auth.models import authenticate
from django.contrib.auth import login, logout
from .models import User_Details

# Create your views here.

def Home(request):
    return render(request, "index.html")

def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user_exists=User_Details.objects.filter(username__iexact=username).first()
        if user_exists:
            data = {
                "error": "Username already exists!"
            }
        else:
            user = User_Details.objects.create(username=username, password=password, email=email)
            user.save()
            data = {
                "success": "User created successfully!"
            }
    else:
        data = {
            "error": "Invalid request method!"
        }
        
    return render(request, "register.html", data)