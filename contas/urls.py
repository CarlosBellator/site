from django.contrib import admin
from django.urls import path
from contas.views import cadastro, login, logout, conta, atualizar_nome, upload_foto_perfil

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path('conta/', conta, name='conta'),
    path('atualizar_nome/', atualizar_nome, name='atualizar_nome'),
    path('upload_foto_perfil/', upload_foto_perfil, name='upload_foto_perfil'),
]