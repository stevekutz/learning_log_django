""" Define URL patterns for user """

from django.urls import path, include  # for login page
from . import views   # for registration page

app_name = 'users'

urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),
    # Define URL pattern for registration
    path('register/', views.register, name = 'register'),

]