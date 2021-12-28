from django.urls import path

from feed.api.views import feed_list, feed_detail
from feed.api.views import FeedViewSet

urlpatterns = [
    path('', feed_list),
    path('<int:pk>/', feed_detail),
]
