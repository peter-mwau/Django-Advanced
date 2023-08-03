from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login,login, logout
# from .models import User_Detail
from django.contrib.auth.models import User
from myapp.models import CustomUser


# Create your views here.

def Home(request):
    return render(request, "homepage.html")

def About(request):
    return render(request, "about.html")

def Services(request):
    return render(request, "services.html")

def user_login(request):
    print("Reached the user_login view.")
    if request.method == "POST":
        print("Received POST request.")
        username = request.POST["username"]
        password = request.POST["password"]
        # user = User_Detail.objects.all()
        user = authenticate(username=username, password=password)

        if user is not None: #
            print("Authentication successful. User:", user)
            login(request, user)
            return redirect("home")  # Replace "home" with the name of your homepage URL
        else:
            print("Authentication failed.")
            data = {
                "error": "Invalid username or password!"
            }
            return render(request, "index.html", data)
    else:
        print("Received GET request.")
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
        user_exists=CustomUser.objects.filter(username__iexact=username).first()
        if user_exists:
            data = {
                "error": "Username already exists!"
            }
        else:
            user = CustomUser.objects.create_user(username=username, password=password, email=email)
            user.save()
            data = {
                "success": "User created successfully!"
            }
    else:
        data = {
            "error": "Invalid request method!"
        }
        
    return render(request, "register.html", data)