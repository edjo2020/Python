"""cadastros URL Configuration"""
#from django.conf.urls import patterns, include, url
#from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include, re_path
#from django.conf.urls import patterns
from cadastros.core import views
from cadastros.clientes import views
admin.autodiscover()

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('cadastros.core.urls')),
    path('^contato/$', include('cadastros.core.urls')),
    path('clientes', include('cadastros.clientes.urls')),
]