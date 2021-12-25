from django.contrib import admin
from django.urls import path, include
from landing.views import home_view
urlpatterns = [
    path('accounts/', include('account.urls')),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('admin/', admin.site.urls),
    path('feeds/', include('feed.urls')),
    path('notifications/', include('notification.urls')),
    path('', include('landing.urls')),

]
