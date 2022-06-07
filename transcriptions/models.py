from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Transcription(models.Model):
    song_name = models.CharField(max_length=30)
    artist_name = models.CharField(max_length=30)
    featured_image = CloudinaryField("image")
    chart = CloudinaryField("file")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transcriber"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["song_name", "artist_name"]

    def __str__(self):
        return f"{self.song_name} by {self.artist_name}"
