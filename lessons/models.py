from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Lesson(models.Model):

    STATUS = (("Draft", 0), ("published", 1))
    LESSON_TYPE = (("txt", "Text"), ("vid", "Video"))

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    video = CloudinaryField("Video Lesson", use_filename=True)
    body = models.TextField(max_length=500)
    type = models.CharField(max_length=3, choices=LESSON_TYPE)
    status = models.IntegerField(default=0, choices=STATUS)
    author = models.ForeignKey(
        User, related_name="drum_lesson", on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
