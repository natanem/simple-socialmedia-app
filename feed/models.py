from django.db import models
from django.conf import settings
from django.urls import reverse


class Feed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feeds', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
     
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='feeds_liked', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.content[:100]

    def get_absolute_url(self):
        return reverse("feed:feed_detail", kwargs={"pk": self.pk})

    
    
class Comment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)