from django.contrib import admin
from django.urls import path
from home.views import index, process_graph_request, upload_file, generate_graph, download_graph_3d

urlpatterns = [
    path('', index, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('process_graph_request/', process_graph_request, name='process_graph_request'),
    path('generate_graph/', generate_graph, name='generate_graph'),
    path('download_graph_3d/<int:graph_id>/', download_graph_3d, name='download_graph_3d'),
]