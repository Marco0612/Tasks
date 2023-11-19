

from collections import deque

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from pyexpat import model
from typing_extensions import Required

# Create your models here.

class User(AbstractUser):
    pass
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    due_date =  models.DateField(auto_now=True)
    relevanse = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    description =  models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="usuarios")
    is_active = models.BooleanField(default=True)
