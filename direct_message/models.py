from django.db import models
from django.conf import settings

class Conversation(models.Model):
    user_one = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    user_two= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.user_two.username

class Message(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_from')
    user_to= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_to')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(blank=True, null=True)
    seen = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
