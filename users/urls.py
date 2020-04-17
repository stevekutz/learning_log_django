""" Define URL patterns for user """

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),

]