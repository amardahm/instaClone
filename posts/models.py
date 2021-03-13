from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    publisher = models.ForeignKey(User,on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=timezone.now())
    image = models.ImageField(upload_to="post_images")
    def __str__(self):
        return self.caption


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length=100,blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now())


class Like(models.Model):
    liker = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now())

