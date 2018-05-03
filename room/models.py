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
    image = models.ImageField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    date_entry = models.DateTimeField()
    date_departure = models.DateTimeField()
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)


class Bill(models.Model):
    user = models.ForeignKey(User)
    room = models.ForeignKey(Room)
    reservation = models.ForeignKey(Reservation)
    date = models.DateTimeField(auto_now_add=True)
    subtotal = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)