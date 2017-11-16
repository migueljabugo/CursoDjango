"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from app.models import SerieTV
from app.forms import FormSerieTV

def home(request):
	assert isinstance(request, HttpRequest)
	series = SerieTV.objects.all()
	return render(
        request,
        'app/index.html',
        {
            'title':'Inicio',
			'series':series,
        }
    )

def notFound(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/404.html',
		{
            'title':'Pagina no encontrada',
        }
	)

def ver_serie(request, id):
	assert isinstance(request, HttpRequest)
	serie = SerieTV.objects.get(pk=id)
	return render(
		request,
		'app/ver_serie.html',
		{
			'title':'Ver serie',
			"serie":serie,
		}
	)

def borrar_serie(request, id):
	assert isinstance(request, HttpRequest)
	serie = SerieTV.objects.get(pk=id)
	serie.delete()
	return HttpResponseRedirect('/')


def crear_serie(request):
	assert isinstance(request, HttpRequest)
	if (request.method == 'POST'):
		#Guardar Formulario relleno
		formulario = FormSerieTV(request.POST)
		if (formulario.is_valid()):
			serie = formulario.save()
			return HttpResponseRedirect('/serie/' + str(serie.id))

	elif (request.method == 'GET'):
		#Peticion de formulario, mandar uno
		return render(
			request,
			'app/form_serie.html',
			{
				'title':'Nueva serie',
				'action':'/crear',
				'form': FormSerieTV(),
			}
		)
	else:
		return render(request, 'app/404.html')


def modificar_serie(request, id):
	assert isinstance(request, HttpRequest)
	serie = SerieTV.objects.get(pk=id)
	if (request.method == 'POST'):
		formulario = FormSerieTV(request.POST, instance=serie)
		if (formulario.is_valid()):
			serie = formulario.save()
			return HttpResponseRedirect('/serie/' + str(serie.id))
	elif (request.method == 'GET'):
		return render(
			request,
			'app/form_serie.html',
			{
				'title':'Editar serie',
				'action':'/modificar/' + str(serie.id),
				'form': FormSerieTV(instance = serie),
				"serie":serie,
			}
		)
	else:
		return render(request, 'app/404.html')

def archivo(request, parametro):
	if(parametro!="genero" and parametro!="productora" and parametro!="fecha_publicacion"):
		return render(request, 'app/404.html')

	lista = SerieTV.objects.values_list(parametro, flat=True).distinct().order_by(parametro).reverse()
	diccionario = {}
	titulo =""
	if(parametro=="genero"):
		titulo="Generos"
		diccionario = SerieTV.generosByLista(lista)
	else:
		for x in lista:
			diccionario[x]=x
		if(parametro=="productora"):
			titulo ="Productoras"
		elif(parametro=="fecha_publicacion"):
			titulo ="Años de publicacion"
			
	return render(
		request, 
		'app/archivo.html',
		{
			'title':titulo,
			'parametro':parametro,
			'lista':diccionario
		}
	)

def listado(request, parametro, id):
	lista = []
	titulo=""
	title=id
	if(parametro=="genero"):
		titulo="Genero"
		lista = SerieTV.objects.filter(genero=id).values_list('id', 'titulo')
		title=SerieTV.generoById(id)
	elif(parametro=="productora"):
		titulo="Productora"
		lista = SerieTV.objects.filter(productora=id).values_list('id', 'titulo')
	elif(parametro=="fecha_publicacion"):
		titulo="Años de publicacion"
		lista = SerieTV.objects.filter(fecha_publicacion=id).values_list('id', 'titulo')
	
	if(len(lista)==0):
		return render(request, 'app/404.html')
	else:
		return render(
			request, 
			'app/listado.html',
			{
				'title':title,
				'lista':lista
			}
		)