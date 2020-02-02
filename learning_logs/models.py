from django.db import models

# Create your models here.

class Topic(models.Model):
    """ Topic that the use in learning about """
    text = models.CharField(max_length=200) # allocates 200 chars in database
    data_added = models.DateTimeField(auto_now_add=True) # sets to current data/time when new topic created
    def __str__(self):
        """ Return a string representation of the model """
        return self.text