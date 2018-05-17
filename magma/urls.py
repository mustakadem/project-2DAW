
from django.conf.urls import include, url
from django.contrib import admin
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^rooms/', include('room.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', views.home, name='home'),
]