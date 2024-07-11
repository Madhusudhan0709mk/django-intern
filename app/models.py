from django.db import models

class DataEntry(models.Model):
    intensity = models.FloatField()
    likelihood = models.FloatField()
    relevance = models.FloatField()
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # Add other fields as necessary
