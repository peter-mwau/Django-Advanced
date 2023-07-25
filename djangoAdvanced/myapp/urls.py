from django.contrib import admin
from django.urls import path
from . views import Home, Register

urlpatterns = [
    path('', view=Home, name='home'),
    path('register/', view=Register, name='register'),
]
