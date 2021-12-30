from django.urls import path

from .views import home_view
from landing.views import search
app_name = 'landing'
urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search, name="search" ),
]
