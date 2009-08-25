from django.http import Http404
from django.shortcuts import render_to_response
from albastryde.cooperativas.models import *
from albastryde.lugar.models import *
from forms import *

# Create your views here.
def comeindex(request):
	F = FormLugar(request.GET)
	query = request.GET.get('departamentos', '')
	if query:
		j = Municipio.objects.filter(departamento=query)
		return render_to_response("/cooperativas/lista-cooperativa.html", {'j':j})
	else:
		k = Departamento.objects.all()
		return render_to_response("/cooperativas/lista-cooperativa.html", locals())
	
def coopmun(request, mun_id):
	a = Cooperativa.objects.filter(municipio__numero=mun_id)
	return render_to_response("/cooperativas/municipio.html", {'a': a})

def verdetalle(request, deta_id):
	c = Cooperativa.objects.filter(id=deta_id)
	return render_to_response("/cooperativas/detalle.html", {'c':c})

def detacompleto(request, p_id):
	b = Detallecoop.objects.filter(cooperativa=p_id)
	return render_to_response("/cooperativas/completo.html", {'b':b})
