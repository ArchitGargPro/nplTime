from django.conf.urls import include, url

from mytime import views

urlpatterns = [
    url(r'^$', views.time, name='time'),
]