from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    thumbnail = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(50, 50)],
        format="JPEG",
        options={"quality": 80},
    )

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )

    def __str__(self):
        return self.title
