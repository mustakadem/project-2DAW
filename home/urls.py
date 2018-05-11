from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^events/$', views.Events.as_view()),
    url(r'^form/reservate/', views.form_reservate)
]

urlpatterns = format_suffix_patterns(urlpatterns)