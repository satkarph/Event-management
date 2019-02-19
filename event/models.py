from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=300, blank=False)
    date = models.DateTimeField(blank=False)
    venue  = models.TextField(max_length=300,blank=False)
    venue_url=models.URLField(blank=True, null=True)
    code = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.event_name

    # def get_absolute_url(self):
    #     return reverse("event:list")

