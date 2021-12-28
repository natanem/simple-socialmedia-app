from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
            
        return {
            'notification_counts' : Notification.objects.filter(target=request.user, is_seen=False).count
        }
    return {'notifications_counts': 0}