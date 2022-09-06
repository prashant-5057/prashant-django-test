from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    total_interests = models.PositiveIntegerField(default=0)
    event_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['total_interests']

#class Review(models.Model):
#   rate = models.ForeignKey(Event,on_delete=models.CASCADE,default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    