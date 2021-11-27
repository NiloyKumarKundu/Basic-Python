from django.db import models

# Create your models here.

class Feature(models.Model):
    # id: int       // We don't need id, because every model has a default id
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

