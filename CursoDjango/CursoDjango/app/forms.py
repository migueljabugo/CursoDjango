"""
Definition of forms.
"""

from django import forms
from app.models import SerieTV

#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _

class FormSerieTV(forms.ModelForm):
	class Meta:
		model = SerieTV
		fields = ("titulo", 
			'productora', 
			'fecha_publicacion', 
			'temporadas', 
			'genero', 
			'estado'
			)


