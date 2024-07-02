from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year_of_forming = models.PositiveIntegerField()
    number_of_events = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.country}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bands = models.CharField(max_length=255, null=True, blank=True)
    isOpenAirEvent = models.BooleanField('Open Air Event', default=False)

    def __str__(self):
        return f"{self.name} - {self.date_time}"


class BandEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.name} - {self.band}"
