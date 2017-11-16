"""
Definition of models.
"""

from django.db import models

class SerieTV(models.Model):
	titulo = models.CharField(max_length=30)
	productora = models.CharField(max_length=20)
	fecha_publicacion = models.IntegerField()
	temporadas = models.IntegerField()
	GENEROS = (
		(0, "Ciencia Ficcion"),
		(1, "Comedia"),
		(2, "Policiaca"),
		(3, "Terror"),
		(4, "Animacion"),
		(5, "Accion"),
		(6, "Drama"),
		(7, "Romance"),
		(8, "Documental"),
		(9, "Historia"),
		)
	genero = models.IntegerField(choices = GENEROS)
	ESTADO = (
		(0, "En produccion"),
		(1, "En emision"),
		(2, "Finalizada"),
		(3, "Cancelada"),
		)
	estado = models.IntegerField(choices = ESTADO)

	def generosByLista(lista):
		diccionario ={}
		for num, nombre in SerieTV.GENEROS:
				for item in lista:
					if (num==item):
						diccionario[num]=nombre
		return diccionario
	
	def generoById(id):
		for num, nombre in SerieTV.GENEROS:
			if (num==int(id)):
				return nombre
		return ""
				
