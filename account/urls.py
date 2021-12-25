from django.urls import path

from .views import signup, profile_view, follow_view, followers_list, following_list

urlpatterns = [
    path('register/', signup, name='signup'),
    path('profile/', profile_view, name= 'profile'),
    path('profile/<int:pk>', profile_view, name= 'profile'),
    path('profile/<int:pk>/follow', follow_view, name= 'follow'),
    path('profile/<int:pk>/followers', followers_list, name= 'followers_list'),
    path('profile/<int:pk>/following', following_list, name= 'following_list'),
]
