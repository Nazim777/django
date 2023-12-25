from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    def __str__(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title


