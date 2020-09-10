from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        "Recipe", symmetrical=False, related_name="favorites", blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=80)
    description = models.TextField(default='')
    time_required = models.CharField(max_length=24, default='')
    instructions = models.TextField(default='')

    def __str__(self):
        return f"{self.title} - {self.author.name}"
