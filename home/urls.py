from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^reservate/', views.reservate_calendar),
    url(r'^(?P<room_id>[0-9]+)/booking/(?P<book_id>[0-9]+)/delete/$', views.delete_calendar)
]

