from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    poemName=models.CharField(max_length=50)
    content=models.TextField()
    