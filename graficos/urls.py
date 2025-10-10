from django.contrib import admin
from django.urls import path
from graficos.views import history

urlpatterns = [
    path('',history, name='history')
]