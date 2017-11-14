"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import SerieTV

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