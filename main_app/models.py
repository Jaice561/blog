from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    thought = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='0')



