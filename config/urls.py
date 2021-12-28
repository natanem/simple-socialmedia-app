from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from landing.views import home_view

from feed.models import Feed
from account.models import Profile
from django.contrib.auth.models import User
def search(request):
    query = request.GET.get('query')
    feeds = Feed.objects.filter(content__icontains=query)
    users = User.objects.filter(username__icontains=query)
    user_ids = [user.id for user in users]
    print(user_ids)
    profiles = Profile.objects.filter(id__in=user_ids)
    context ={
        'feeds' : feeds,
        'profiles' : profiles
    }
    print(query)
    return render(request, "search.html", context)

urlpatterns = [
    path('accounts/', include('account.urls')),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('admin/', admin.site.urls),
    path('feeds/', include('feed.urls')),
    path('notifications/', include('notification.urls')),
    path('search/', search, name="search" ),
    path('', include('landing.urls')),

    # api routes

    path('api/feeds/', include(('feed.api.urls', 'feed_api'))),

]
