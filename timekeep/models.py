from django.contrib.auth.models import User
from django.db import models

from datetime import timedelta

class Task(models.Model):
    task = models.CharField(max_length=140)
    description = models.CharField(max_length=280, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    start = models.DateTimeField(null=True, blank=True)
    pause_begin = models.DateTimeField(null=True, blank=True)
    paused = models.DurationField(default=timedelta)
    elapsed = models.DurationField(null=True, blank=True)
    elapsed_str = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.task} de {self.user}"
