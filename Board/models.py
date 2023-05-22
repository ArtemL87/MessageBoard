from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    category_com = models.ManyToManyField(to='Category', through='PostCategory')
    title_post = models.CharField(max_length=50)
    text_post = models.TextField()

    def __str__(self):
        return self.title_post


class PostCategory(models.Model):
    post_com = models.ForeignKey('Post', on_delete=models.CASCADE)
    category_com = models.ForeignKey('Category', on_delete=models.CASCADE)



class Comment(models.Model):
    post_com = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_com = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)