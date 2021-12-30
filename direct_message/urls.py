from django.urls import path

from .views import message_list_view, message_detail_view, message_send_view

app_name = 'direct_message'

urlpatterns = [
    path('', message_list_view, name='message_list'),
    path('<int:pk>/send/', message_send_view, name='message_send'),
    path('<int:pk>/', message_detail_view, name='message_detail'),
]
