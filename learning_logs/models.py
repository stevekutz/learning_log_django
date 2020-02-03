from django.db import models

# Create your models here.

class Topic(models.Model): # inherit from Django's base Model class 
    """ Topic that the use in learning about """
    text = models.CharField(max_length=200) # allocates 200 chars in database
    data_added = models.DateTimeField(auto_now_add=True) # sets to current data/time when new topic created
    def __str__(self):
        """ Return a string representation of the model """
        return self.text


class Entry(models.Model): # inherit from Django's base Model class
    """ Something specifis learned about a topic """  
     # Each topic is assigned a specific key ID when created      
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)  # connects entry to a topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # tells Django to use  'Entries' deal with mutliple entries
    # otherwise Django creates 'Entrys'
    class Meta:
        verbose_name_plural = 'entries'

    # show only first 5 chars of text
    def __str__(self):
        """ Return a string represenation of the model """
        return self.text[:50] + "..."
