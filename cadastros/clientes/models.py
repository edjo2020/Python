from django.db import models

# Criacao de modelos da apalicacao.

class ClientesManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
		#	name__icontains=query,
		#	slug__icontains=query
        models.Q(name__icontains=query) | \
		models.Q(slug__icontains=query)		
		) 	


class clientes(models.Model):
	name 		= models.CharField('Nome',max_length=100)
	username	= models.CharField('Usuario',max_length=20)
	email 		= models.CharField('email',max_length=50)
	slug 		= models.SlugField('Atalho')
	create_at 	= models.DateTimeField(
		'Criado em',auto_now_add=True
	)
	update_at 	= models.DateTimeField('Atualizado em',auto_now=True)


	objects 	= ClientesManager()		

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'	
		ordering=['name']