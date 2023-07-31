from django.contrib import admin
from . models import User_Detail

class User_DetailAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


admin.site.register(User_Detail, User_DetailAdmin)
