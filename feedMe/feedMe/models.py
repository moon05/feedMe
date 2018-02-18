from __future__ import unicode_literals

from django.db import models


class Directory(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    netid = models.CharField(max_length=30)
    studentid = models.IntegerField()
    dorm = models.CharField(max_length=10)
    balance = models.IntegerField()
    location = models.TextField(max_length=30)

    class Meta:
        db_table = 'Directory'
        app_label = "feedMe"
