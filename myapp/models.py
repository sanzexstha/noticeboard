from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



 
class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    text = models.TextField(null=False )
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents/', null=True, blank=True)


class PostLike(models.Model):
    post= models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.post)} - {str(self.user)} - {self.created_at}"
 
class Comment(models.Model):
    commented_by= models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comment = models.TextField(help_text=_('Should contain only text'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

 
 
    
