from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic  # import Topic model to be registered
admin.site.register(Topic)  # regsters Topic to be managed via admin site 
