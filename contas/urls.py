from django.contrib import admin
from django.urls import path
from contas.views import cadastro, login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]