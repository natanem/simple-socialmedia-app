from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Feed, Comment
from notification.models import Notification

from .forms import FeedCreateForm, CommentCreateForm

@login_required
def feed_list(request):
    feeds = Feed.objects.all()
    feed_form = FeedCreateForm()
    comment_form = CommentCreateForm
    context = {'feeds' : feeds, 'feed_form': feed_form, 'comment_form': comment_form}
    return render(request, 'feed/feed_list.html', context)

def feed_detail(request, pk):
    feed = get_object_or_404(Feed, pk=pk)
    comments = feed.comments.all()
    form = CommentCreateForm()
    context = {
        'feed': feed,
        'comments': comments,
        'form' : form
    }
    return render(request, 'feed/feed_detail.html', context)

@login_required
def feed_create_view(request):
    if request.method == 'POST':
        form = FeedCreateForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.user = request.user
            feed.save()
            return redirect('feed:feed_list')
    else:
        form = FeedCreateForm()

    context = {
        'form' : form
    }
    return render(request, 'feed/feed_create.html', context)


@login_required
def like_feed(request, pk):
    feed = get_object_or_404(Feed, pk=pk)

    if request.user in feed.likes.all():
        feed.likes.remove(request.user)
        feed.save()
    else:
        feed.likes.add(request.user)
        if request.user != feed.user:
            Notification.objects.create(user=request.user, type='like', target_model=feed.pk, target=feed.user)
        feed.save()
    
    return redirect('feed:feed_list')

@login_required
def comment_feed(request, pk):
    feed = get_object_or_404(Feed, pk=pk)

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.feed = feed
            new_comment.save()
            # return redirect(feed)
            if new_comment.user != feed.user:
                Notification.objects.create(user=request.user, type='comment', target_model=feed.pk, target=feed.user)
            return redirect('feed:feed_list')

    else:
        form = CommentCreateForm()

    context = {
        'feed': feed,
        'form': form
    }
    
    return render(request, 'feed/comment_create.html', context)


def api_like_feed(request):
    
    response = {
        'ok': 'ok',

    }
    return JsonResponse(response)