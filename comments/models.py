from django.db import models
from django.contrib.auth import get_user_model
from ads.models import Ad

User = get_user_model()

class Comment(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.ad}"
