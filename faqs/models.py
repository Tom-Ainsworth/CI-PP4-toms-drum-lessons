from django.db import models


class Question(models.Model):
    """Model for Frequently asked questions"""

    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
