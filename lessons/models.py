from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Lesson(models.Model):

    STATUS = ((0, "Draft"), (1, "published"))
    LESSON_FORMAT = (("txt", "Text"), ("vid", "Video"))

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    video = CloudinaryField("Video Lesson", use_filename=True)
    body = models.TextField(max_length=500)
    format = models.CharField(max_length=3, choices=LESSON_FORMAT)
    status = models.IntegerField(default=0, choices=STATUS)
    author = models.ForeignKey(
        User, related_name="drum_lesson", on_delete=models.PROTECT
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} by {self.author}"
