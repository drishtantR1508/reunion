from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.TextField(max_length=50)
    lastname=models.TextField(max_length=50,blank=True)
    email = models.EmailField(unique=True,blank=True)
    contact=models.PositiveIntegerField(blank=True)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    following = models.ManyToManyField(User,related_name="following",blank=True)

    def __str__(self):
        return self.user.username

    def count_followers(self):
        return self.followers.count()

    def count_following(self):
        return self.following.count()