from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.

class Event(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="project",null=False)
    event_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    venue  = models.TextField(max_length=300,blank=True)
    venue_url=models.URLField(blank=True, null=True)
    code = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.event_name

    def __unicode__(self):
        return unicode(self.user)

    # def get_absolute_url(self):
    #     return reverse("event:list")

