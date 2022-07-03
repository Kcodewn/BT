
from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    name = models.CharField(max_length=500, null=True)
    STATUS = (
            ('New Tickets', 'New Tickets'),
            ('In Progress', 'In Progress'),
            ('Urgent Tickets', 'Urgent Tickets'),
            ('Resolved', 'Resolved'),
                )
    status = models.CharField(max_length=500, null=True, choices=STATUS)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    STATUS = (
            ('New Project', 'New Project'),
            ('In Progress', 'In Progress'),
            ('Finished', 'Finished'),
                )
    status = models.CharField(max_length=500, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

