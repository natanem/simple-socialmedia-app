from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from landing.views import home_view

from feed.models import Feed
from account.models import Profile
from django.contrib.auth.models import User


urlpatterns = [
    path('accounts/', include('account.urls')),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('admin/', admin.site.urls),
    path('feeds/', include('feed.urls')),
    path('notifications/', include('notification.urls')),
    path('messages/', include('direct_message.urls')),
    path('search/', include('landing.urls') ),
    path('', include('landing.urls')),

    # api routes

    path('api/feeds/', include(('feed.api.urls', 'feed_api'))),

]
