from django.urls import path, include, re_path
from cadastros.clientes import views

urlpatterns = [
    path('clientes', views.clientes, name='clientes'),
]  