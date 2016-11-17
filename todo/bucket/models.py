from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Base(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Bucketlist(Base):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name='bucketlists', on_delete=models.CASCADE)


class BucketlistItem(Base):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(
        Bucketlist, related_name='items', on_delete=models.CASCADE)
