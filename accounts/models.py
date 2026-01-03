from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    phone = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="user_avatars/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   

    def __str__(self):
        return f"Profile of {self.user.email}"
