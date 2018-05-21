from django.conf.urls import url

from . import views

room_detail = views.RoomDetail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', room_detail, name='detail'),
    url(r'^(?P<room_id>[0-9]+)/reservation/$', views.reserva, name='reservation'),
    url(r'^(?P<room_id>[0-9]+)/booking/(?P<book_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^events/$', views.EventsList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventsDetail.as_view()),
]