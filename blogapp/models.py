from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.name.username

class Category(models.Model):
    cat_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.cat_name 

class Post(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField()
    desc = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} by {}".format(self.title, self.author.name)