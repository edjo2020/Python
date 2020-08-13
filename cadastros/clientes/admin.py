from django.contrib import admin

# Registros models.
from .models import clientes

class ClientesAdmin(admin.ModelAdmin):
	list_display 	= ['name', 'username', 'email']
	search_fields	= ['name', 'username', 'slug', 'email']

admin.site.register(clientes,ClientesAdmin)

