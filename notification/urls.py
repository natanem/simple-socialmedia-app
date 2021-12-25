from django.urls import path
from .views import  notification_list, notification_detail

app_name = 'notification'
urlpatterns = [
    path('', notification_list, name='notification_list'),
    path('<pk>/', notification_detail, name='notification_detail'),
]
