from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', related_name='followers', through='Relationship', symmetrical=False)
    # following = models.ManyToManyField('self', through='Contact', related_name='followers', symmetrical=False)
    
    def __str__(self):
        return f'profile for {self.user}'


class Relationship(models.Model):
    user_from = models.ForeignKey('Profile', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('Profile', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

# class Contact(models.Model)
#     user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
#     user_to = models.ForeignKey('auth.User', related_name='rel_to_set', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True, db_index=True)
#     class Meta:
#         ordering = ('-created',)
#     def __str__(self):
#         return f'{self.user_from} follows {self.user_to}'