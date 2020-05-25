from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    views = models.IntegerField(default=0) 
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name =  models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message =  models.TextField()

    def __str__(self):
        return self.name

    

class Comment(models.Model):
    name =  models.CharField(max_length=200)
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete= models.CASCADE , related_name="post")
    reply =models.ForeignKey('self', on_delete= models.CASCADE , null = True, related_name="replies")
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content

