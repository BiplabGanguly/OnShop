from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    web_admin = models.CharField(max_length=500, default="false")
    address = models.TextField()
    user_pin = models.CharField(max_length=255,blank=True)
    user_dist = models.CharField(max_length=255,blank=True)
    user_state = models.CharField(max_length=255,blank=True)

    def __str__(self) -> str:
        return self.user.first_name
    

class State(models.Model):
    state_name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.state_name
