from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login,login, logout
from .models import User_Detail

# Create your views here.

def Home(request):
    return render(request, "index.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Replace "home" with the name of your homepage URL
        else:
            data = {
                "error": "Invalid username or password!"
            }
            return render(request, "index.html", data)
    else:
        data = {
            "error": "Invalid request method!"
        }
        return render(request, "index.html", data)
    
def user_logout(request):
    logout(request)
    return redirect("login")  # Replace "login" with the name of your login URL

def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user_exists=User_Detail.objects.filter(username__iexact=username).first()
        if user_exists:
            data = {
                "error": "Username already exists!"
            }
        else:
            user = User_Detail.objects.create(username=username, password=password, email=email)
            user.save()
            data = {
                "success": "User created successfully!"
            }
    else:
        data = {
            "error": "Invalid request method!"
        }
        
    return render(request, "register.html", data)