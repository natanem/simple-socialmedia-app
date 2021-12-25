from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from feed.models import Feed
from account.models import Profile, Relationship
from notification.models import Notification

from .forms import UserForm


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user = new_user)
            return redirect('accounts:login')
    else:   
      form = UserForm()
    context = {
        'form' : form
    }
    return render(request, 'registration/signup.html', context)

@login_required
def profile_view(request, pk=None):
    if pk is not None:
        user = get_object_or_404(User, pk=pk)
    else:
        user = request.user
    
    feeds = Feed.objects.filter(user=user)
    context = {
        'user': user,
        'feeds': feeds
    }
    return render(request, 'account/profile.html', context)

def follow_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    found_relation = Relationship.objects.filter(user_from=request.user.profile, user_to=profile).exists()
  
    if found_relation:
        request.user.profile.following.remove(profile)

    else:
        request.user.profile.following.add(profile)
        Notification.objects.create(user=request.user, type='follow', target_model=request.user.profile.pk, target=profile.user)
        

    print(profile.followers.all())
    return redirect('profile', pk=pk)

def followers_list(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    followers = profile.followers.all()
   
   
    context = {
        'profile': profile,
        'followers': followers
    }

    return render(request, 'account/followers_list.html', context)

def following_list(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    following = profile.following.all()

    context = {
        'profile': profile,
        'following': following
    }

    return render(request, 'account/following_list.html', context)
