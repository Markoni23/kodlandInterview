from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)