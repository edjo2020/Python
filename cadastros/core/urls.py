from django.urls import path, include, re_path
from cadastros.core import views
#from cadastros.clientes import views

urlpatterns = [
    path('', views.home),
    path('contato/', views.contato),
#    path('clientes/', views.clientes),
]  