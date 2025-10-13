from django.contrib import admin
from django.urls import path
from contas.views import cadastro, login, logout, conta, atualizar_nome, upload_foto_perfil, alterar_senha, conta_alterar_senha_mobile


urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path('conta/', conta, name='conta'),
    path('conta/alterar_senha/', conta_alterar_senha_mobile, name='conta_alterar_senha_mobile'),
    path('atualizar_nome/', atualizar_nome, name='atualizar_nome'),
    path('upload_foto_perfil/', upload_foto_perfil, name='upload_foto_perfil'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
]