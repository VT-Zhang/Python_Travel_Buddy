from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    b_date = models.DateField()
    e_date = models.DateField()
    plan = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_in_trip')

class Group(models.Model):
    user = models.ForeignKey(User, related_name='useruser')
    trip = models.ForeignKey(Trip, related_name='triptrip')
