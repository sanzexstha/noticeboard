from django.db import models
from django.contrib.auth.models import User


 
class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    image = models.ImageField(upload_to='documents/', null=True, blank=True)
    text = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def comment(self):
        comments = Comment.objects.filter(post_id=self.id)
        return comments
        

class PostLike(models.Model):
    Post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE)


class Comment(models.Model):
    commented_by = models.ForeignKey(User, related_name='users_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.user.username)

 
    
