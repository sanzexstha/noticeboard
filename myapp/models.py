from django.db import models
from django.contrib.auth.models import User


 
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_by')
    image = models.ImageField(upload_to='documents/', null=True, blank=True)
    text = models.TextField(null=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def comment(self):
        comments = Comment.objects.filter(post_id=self.id)
        return comments


class PostLike(models.Model):
    post= models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.post)} - {str(self.user)} - {self.created_at}"



class Comment(models.Model):
    commented_by= models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.user.username)

 
    
