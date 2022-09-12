from django.db import models
from finalproject.models import finalproject

# Create your models here.


class Post (models.Model):
    auther = models.ForeignKey(finalproject, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.TextField()
