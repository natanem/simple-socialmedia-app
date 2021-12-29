from django.db import models
from django.conf import settings

class Conversation(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations')
    user_to= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations')
    messages = models.ForeignKey('Message', no_delete=models.CASCADE, blank=True, null=True)


class Message(models.Model):
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
