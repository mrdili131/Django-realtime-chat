from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
   #profile_image = models.ImageField('upload_to')
    bio = models.CharField(max_length=150,default="")
    number = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    verified = models.BooleanField(default=False)
