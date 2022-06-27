from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, related_name="reviewer", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"
