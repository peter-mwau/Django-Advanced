from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.username
