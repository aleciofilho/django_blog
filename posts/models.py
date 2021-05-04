from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=modles.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)