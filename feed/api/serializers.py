from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from django.contrib.auth.models import User, Group
from feed.models import Feed, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']



class FeedSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Feed
        fields = ['id', 'content', 'created']


