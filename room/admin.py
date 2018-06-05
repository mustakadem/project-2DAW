# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Room, Booking, Image

admin.site.register(Room)

admin.site.register(Booking)

admin.site.register(Image)
