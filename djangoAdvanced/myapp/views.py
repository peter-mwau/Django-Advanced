from django.shortcuts import render
import requests

# Create your views here.

def Home(request):
    return render(request, "index.html")
