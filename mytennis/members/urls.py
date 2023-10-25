from django.urls import path
from . import views


urlpatterns = [
    path ('myfist/', views.myfist, name='myfist'),
    path ('cicak/', views.cicak, name='cicak'),
]