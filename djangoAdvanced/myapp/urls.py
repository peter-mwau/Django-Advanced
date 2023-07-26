from django.contrib import admin
from django.urls import path
from . views import Home, Register, user_login, user_logout

urlpatterns = [
    path('', view=user_login, name='login'),
    path('register/', view=Register, name='register'),
    path('home/', view=Home, name='home'),
    path('', view=user_logout, name='logout'),
]
