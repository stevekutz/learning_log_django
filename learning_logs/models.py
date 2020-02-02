from django.db import models

# Create your models here.

class Topic(model.Model):
""" Topic that the use in learning about """
    text = models.CharField(max_length=200)
    data_added = models.DataTimeField(auto_now_add=True)
    def __str__(self):
        """ Return a string representation of the model """
        return self.text