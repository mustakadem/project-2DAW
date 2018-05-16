from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.RoomDetail.as_view(), name='detail'),
    url(r'^(?P<room_id>[0-9]+)/reservation/$', views.reserva, name='reservation'),
    url(r'^events/$', views.EventsList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventsDetail.as_view()),
]