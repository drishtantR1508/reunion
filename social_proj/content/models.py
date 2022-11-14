from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Post(models.Model):
    written_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1500)
    created_at = models.DateTimeField(default=datetime.now)
    like = models.ManyToManyField(User,related_name="post_liked",blank=True)

    def count_likes(self):
        return self.like.count()
    def __str__(self):
        return self.title


class Comments(models.Model):
    written_by = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default="IT",related_name="comments")
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.written_by.username+" on "+self.post.title