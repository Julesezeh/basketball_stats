from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=300)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.username