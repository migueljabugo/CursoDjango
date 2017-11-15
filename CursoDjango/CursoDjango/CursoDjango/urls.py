"""
Definition of urls for CursoDjango.
"""

#from datetime import datetime
from django.conf.urls import url
#import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    url(r'^$', app.views.home, name='home'),
	url(r'^serie\/(?P<id>[0-9]+)$', app.views.ver_serie, name='ver_serie'),
	url(r'^borrar\/(?P<id>[0-9]+)$', app.views.borrar_serie, name='borrar_serie'),
	url(r'^modificar\/(?P<id>[0-9]+)$', app.views.modificar_serie, name='editar_serie'),
	url(r'^crear\/{0,1}$', app.views.crear_serie),
	url(r'^archivo\/(?P<parametro>[a-zA-Z_]+)$', app.views.archivo),
	url(r'', app.views.notFound),

]
