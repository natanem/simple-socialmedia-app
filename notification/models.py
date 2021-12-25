from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPE = (
        ('like', 'Like'),
        ('follow', 'Follow'),
        ('post', 'Post'),
        ('comment', 'Comment')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=NOTIFICATION_TYPE)
    target_model = models.PositiveIntegerField(null=True)
    target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.type