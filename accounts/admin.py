from django.contrib import admin
from django.contrib.auth.models import AbstractUser

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

admin.site.register(User, UserAdmin)

