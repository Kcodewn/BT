
from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    name = models.CharField(max_length=500, null=True)
    ROLE = (
            ('Admin', 'Admin'),
            ('Developer', 'Developer'),
            ('Project Manager', 'Project Manager'),
            ('Submitter', 'Submitter'),
                )
    role = models.CharField(max_length=500, null=True, choices=ROLE)

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
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=500, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=500, null=True)
    POWER = (
            ('Project Manager', 'Project Manager'),
            ('Team Member', 'Team Member'),
                )
    power = models.CharField(max_length=500, null=True, choices=POWER)
    project = models.ManyToManyField(Project)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    name = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    STATUS = (
            ('New Tickets', 'New Tickets'),
            ('In Progress', 'In Progress'),
            ('Urgent Tickets', 'Urgent Tickets'),
            ('Resolved', 'Resolved'),
                )
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=500, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name