from django.db import models

# Create your models here.

class Appinfo(models.Model):
    title = models.CharField(max_length = 50)
    websitename = models.CharField()
    
