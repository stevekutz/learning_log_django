from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model): # inherit from Django's base Model class 
    """ Topic that the use in learning about """
    text = models.CharField(max_length=200) # allocates 200 chars in database
    data_added = models.DateTimeField(auto_now_add=True) # sets to current data/time when new topic created
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        """ Return a string representation of the model """
        return self.text


class Entry(models.Model): # inherit from Django's base Model class
    """ Something specifis learned about a topic """  
     # Each topic is assigned a specific key ID when created  
     # ForeignKey connects entry to a topic & CASCADE tells Django to delete every entry under a topic
     #  when a topic is deleted    
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)  # connects entry to a topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # tells Django to use  'Entries' deal with mutliple entries
    # otherwise Django creates 'Entrys'
    class Meta:
        verbose_name_plural = 'entries'

    # show only first 50 chars of text
    def __str__(self):
        """ Return a string representation of the model """
        # return self.text[:50] + "..."
        return f"{self.text[:50]}..."