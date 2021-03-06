# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Booking(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


# class Bill(models.Model):
#     user = models.ForeignKey(User)
#     room = models.ForeignKey(Room)
#     booking = models.ForeignKey(Booking)
#     date = models.DateTimeField(auto_now_add=True)
#     subtotal = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
#     total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)


class Image(models.Model):
    room = models.ForeignKey(Room)
    image = models.ImageField(upload_to='rooms/images/')

    def __unicode__(self):
        return str(self.image)


class Features(models.Model):
    room = models.OneToOneField(Room)
    slate = models.BooleanField(default=False)
    spotlight = models.BooleanField(default=False)
    capacity = models.IntegerField(default=0)
    chairs = models.IntegerField(default=0)
    wifi = models.BooleanField(default=False)
    sound_system = models.BooleanField(default=False)
    videoConference_equipament = models.BooleanField(default=False)

    def __str__(self):
        return self.room.name
