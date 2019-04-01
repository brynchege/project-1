from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)


def __str__(self):
    return self.titlepython


def snippet(self):
    return self.body[:1] + "..."
