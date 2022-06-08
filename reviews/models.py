from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    author = models.ForeignKey(User, related_name="reviewer", on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=STATUS)

    class Meta:
        ordering = ["author"]

    def __str__(self):
        return self.title
