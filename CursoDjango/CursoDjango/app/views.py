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
				'action':'/modificar',
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
	lista = SerieTV.objects.values_list(parametro, flat=True).distinct()
	

	return render(
		request, 
		'app/archivo.html',
		{
			'title':parametro,
			'lista':lista,
			'generos':generos
		}
	)

