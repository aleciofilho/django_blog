from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)