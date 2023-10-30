from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(unique=True,max_length=100)    
    email = models.EmailField(unique=True)

    
    def __str__(self):
        return self.email
    
    REQUIRED_FIELDS = ['email']
    