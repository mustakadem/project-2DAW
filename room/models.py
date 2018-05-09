# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Room(models.Model):

    name = models.CharField(max_length=30)
    features = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255)
    hours = models.TimeField(null=True, blank=True)
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


class RoomImage(models.Model):
    room = models.ForeignKey(Room)
    url = models.CharField(default=0, max_length=6000)