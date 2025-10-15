from django.contrib import admin
from django.urls import path
from home.views import index, upload_file

urlpatterns = [
    path('', index, name='home'),
    path('upload/', upload_file, name='upload_file'),
]