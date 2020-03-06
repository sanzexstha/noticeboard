from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    image = models.ImageField(upload_to='documents/', null=True, blank=True)


    
