"""Defines URL patters for pizzas app"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]