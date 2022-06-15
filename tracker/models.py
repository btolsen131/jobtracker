from django.db import models
from django.utils import timezone

class Job(models.Model):
    position_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    date_applied = models.DateTimeField(default=timezone.now)
    applied_via = models.CharField(max_length=200)

    def __str__(self):
        return self.position_name

class Interview(models.Model):
    interview_date = models.DateTimeField()
    interviwer = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    thoughts = models.TextField(null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
