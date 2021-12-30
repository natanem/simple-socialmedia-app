from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from feed.models import Feed
from account.models import Profile

def home_view(request):
    if request.user.is_authenticated:
        return redirect('feed:feed_list')
    return render(request, 'landing/home.html')


def search(request):
    query = request.GET.get('query')
    feeds = Feed.objects.filter(content__icontains=query)
    users = User.objects.filter(username__icontains=query)
    
    user_ids = [user.id for user in users]
    print(user_ids)
    profiles = Profile.objects.filter(user__id__in=user_ids)
    context ={
        'feeds' : feeds,
        'profiles' : profiles
    }
    print(query)
    return render(request, "landing/search.html", context)