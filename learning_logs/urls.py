""" Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    # path that shows all topics
    path('topics/', views.topics, name = 'topics'),
    # detail page for a single topic based on topic_id
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # form page for adding new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),
    
    # form page for new entries  
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # form page for editing entries based on entry_id
    path('edit_entry/<int:entry_id>/' , views.edit_entry, name = 'edit_entry'),
    

]

