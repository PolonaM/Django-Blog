from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create a class to represent a blog post

STATUS = ((0, 'Draft'), (1, 'Publish'))

class Post(models.Model): # Model is a class that contains field of data
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True) # When author will create the now content from the admin page the current date and time will ge generated
    slug = models.SlugField(max_length = 200, unique = True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE) #ForeignKey because we will get this data from another table; cascade - if user is deleted from the user database table alos the posts from the user will be created
    status = models.IntegerField(choices = STATUS, default = 0) # choose from draft/published

    def __str__(self):
        return self.title