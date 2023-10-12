from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.TextField(User.USERNAME_FIELD, null=True)
    text = models.TextField()