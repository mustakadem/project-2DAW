# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls  import resolve
from django.core.urlresolvers import reverse
from .models import Room
from .views import reserva
from .forms import NewBooking


class RoomTest(TestCase):
    def setUp(self):
        Room.objects.create(name='SalaPrueba', features='Muy amplia', type='Sala', size=23.0, price=45.0)

    def test_reserva_view_success_status_code(self):
        url = reverse('reservation', kwargs={'room_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_reserva_view_not_found_status_code(self):
        url = reverse('reservation', kwargs={'room_id': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_reserva_url_resolves_board_topics_view(self):
        view = resolve('rooms/1/reservation/')
        self.assertEqual(view.func, reserva)

    def test_contains_form(self):
        url = reverse('reservation', kwargs={'room_id': 1})
        response = self.client.get(url)
        form = response.context_get('form')
        self.assertEqual(form, NewBooking)
