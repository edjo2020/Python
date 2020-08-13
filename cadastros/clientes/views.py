from django.shortcuts import render
from django.http import HttpResponse

def clientes(request):
	template_name='clientes.html'
	return render(request,template_name)
