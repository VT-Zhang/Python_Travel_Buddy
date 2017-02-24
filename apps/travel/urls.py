from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^goto$', views.goto, name='goto'),
    url(r'^travels$', views.home, name='home'),
    url(r'^create$', views.create, name='create'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    url(r'^destination/(?P<id>\d+)$', views.destination, name='destination'),
]
