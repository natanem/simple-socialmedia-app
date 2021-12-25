from django.shortcuts import get_object_or_404, redirect, render

from .models import Notification

def notification_list(request):
    notifications = Notification.objects.filter(target=request.user, is_seen=False)

    context = {
        'notifications' : notifications
    }
    return render(request, 'notification/notification_list.html', context)

def notification_detail(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    notification.is_seen = True
    notification.save()
    if notification.type == 'follow':
        return redirect('profile', pk=notification.target_model)
    return redirect('feed:feed_detail', pk=notification.target_model)
        