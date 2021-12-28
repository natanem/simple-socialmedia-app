from django.urls import path
from .views import feed_list, feed_create_view, comment_feed, like_feed, feed_detail, api_like_feed


app_name = 'feed'
urlpatterns = [
   
    path("", feed_list, name="feed_list"),
    path("", feed_list, name="feed_list"),
    path('<int:pk>/', feed_detail, name='feed_detail'),
    path("create/", feed_create_view, name="feed_create"),
    path("<int:pk>/comments/create", comment_feed, name="comment_feed"),
    path("<int:pk>/likes/add", like_feed, name="like_feed"),
]

