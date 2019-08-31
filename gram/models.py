from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30,default=True)
    last_name = models.CharField(max_length=30,default=True)
    bio = models.CharField(max_length=350,default=True) 
    profile_pic = models.ImageField(upload_to='ProfilePicture/',default=True)
    profile_avatar = models.ImageField(upload_to='AvatorPicture/',default=True)
    date = models.DateTimeField(auto_now_add=True, null= True)  
