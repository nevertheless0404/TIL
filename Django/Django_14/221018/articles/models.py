import imp
from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)

    def __str__(self):
        return self.title
