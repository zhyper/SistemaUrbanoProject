#from pipes import Template


from json import dumps
import json
from django.db.models import Count,Sum
#from msilib.schema import ListView
from pyexpat import model
from django.core import serializers
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from pathlib import Path

#from requests import request


from world.models import GisBaseZonasZreDjango, TZona
from portal.models import Slide, SlideItem, WebsiteName
from zonas.models import Plan, PlanEtapa, PlanMapa, ZonaDensidadPoblacionalTabla, ZonaNivelInstruccionTabla, ZonaPoblacion, ZonaPoblacionTabla

from django.views.decorators.clickjacking import xframe_options_exempt



"""HOME"""
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

@xframe_options_exempt
def Home(request):    

    # zonas = GisBaseZonasZreDjango.objects.all()
    # zonasdata= serializers.serialize("json",zonas)

    websitename = WebsiteName.objects.get(id=1)
    
    zonas = TZona.objects.all().exclude(codigo_zona="CUSCO").order_by('codigo_zona')
    zonasdata= serializers.serialize("json",zonas)

    planes = Plan.objects.all()

    slide = Slide.objects.all()
    slideData = serializers.serialize("json", slide)

    # Metadata OpenGraph----------------------------------------------------------------------------------
    og_title = "Plataforma de Gestión Territorial Provincial Cusco"
    og_description = "Municipalidad Provincial del Cusco"
    og_image = "http://sgot.cusco.gob.pe:90/zre41media/slides/home/banner_planes_1200.jpg"


    context = {
        "title": "Home PGT v2.0",
        "zonasjson": zonasdata,
        "zonas": zonas,
        "slide": slide,
        "planes": planes,
        "WebsiteName": websitename,
        "slidehome": SlideItem.objects.filter(slide=1),
        "slidejson": slideData,
        #og
        "og_title": og_title,
        "og_description": og_description,
        "og_image": og_image,
    }
    #dataJSON = dumps(context)
    #return render(request,'home.html', context)
    return render(request,'home.html', context)



"""TIKARY MAP"""
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def TikaryMap(request):    

    # zonas = GisBaseZonasZreDjango.objects.all()
    # zonasdata= serializers.serialize("json",zonas)
    
    zonas = TZona.objects.all().exclude(codigo_zona="CUSCO").order_by('codigo_zona')
    zonasdata= serializers.serialize("json",zonas)

    context = {
        "title": "Tikary Map v.0.1",
        "zonasjson": zonasdata,
        "zonas": zonas
    }
    #dataJSON = dumps(context)
    #return render(request,'home.html', context)
    return render(request,'tikarymap.html', context)



def SourceWMSHome(request):
    return HttpResponse('Lista de WMS Sources')


def categoriaEdad(req, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Niñez"
        else:
            categoria = "Adolescencia"
    resultado = "<h3>Categoría de la Edad: %s</h3>" %categoria
    
    return HttpResponse(resultado)



def WmsPlantilla(req):
    """
    templateExterna = open( Path(__file__).resolve().parent / 'templates' / 'wms.html' )
    template = Template(templateExterna)
    templateExterna.close()
    document = template.render(context)
    """
    
    context  = {
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'alumnos': [
            { "name": 'joji', "edad": 12, "hovies": [{"name": "futbol"}]},
            { "name": 'allo', "edad": 8, "hovies": [{"name": "voley"},{"name": "ajedrez"}]},
            { "name": 'tioo', "edad": 10, "hovies": [{"name": "basket"},{"name": "PS4"}]},
            { "name": 'nanann', "edad": 9, "hovies": [{"name": "Movies"}]},
        ]
    }
    return render(req, "wms.html", context)




def MapOk(request):
    return render(request,'mapOK.html')    



def MapOk2(request):
    return render(request,'mapOK2.html')    

