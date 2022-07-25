from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Events(models.Model):
    event_title = models.CharField(max_length=500)
    event_description = models.TextField()
    event_snippet = models.CharField(max_length=25)
    event_date_time = models.DateTimeField(default=timezone.now)
    event_location = models.CharField(max_length=100)
    # admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.event_title
    #
    # def get_absolute_url(self):
    #     return reverse('events')