import json

from django.db.models import Count,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response

from planes.models import ParametroUrbanoPDU

from django.db.models.functions import (
   TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond,
 )

from django.db.models import Count

from django.core.serializers.json import DjangoJSONEncoder

from .forms import ConsultaForm, DocumentForm
from .models import Document, Consulta, Editors, Plan, GisBaseZonasZreV2,ZonaCaracterizacionGRDAnalisisVulnerabilidad, ZonaCaracterizacionGRDDeterminacionPeligro, ZonaCaracterizacionLegal, ZonaCaracterizacionSocioeconomica, ZonaConsideracionesGenerales, ZonaDelimitacion, ZonaDensidadPoblacionalTabla, ZonaJustificacion, ZonaMetodologia, ZonaNivelInstruccionTabla, ZonaObjetivos, ZonaPlaneamiento, ZonaPoblacion, PlanMapa, ZonaPoblacionTabla, ZonaPresentacion, GisBaseZonasZreVertices, GisBaseZonasAmbitosVertices

from .models import ViewGraph

from world.models import TZona
from portal.models import Slide, SlideItem, WebsiteName
from api.serializers import ParametroUrbanoSerializer, PlanSerializer, PoblacionZonaSerializer, ZonaSerializer, PlanFullSerializer

# Create your views here.

def ConsultaWebPlan(request):

    message = "Bienvenido a la Consulta Web de Planes de Zonas"

    if request.method=='POST':
        
        miFormulario = ConsultaForm(request.POST, request.FILES)

        if miFormulario.is_valid():
            #creamos una nueva instancia de la clase Consulta
            newConsulta = Consulta(
                email = request.POST.get('email'),
                nombres = request.POST['nombres'],
                apellidos = request.POST['apellidos'],
                tipo_doc_identidad = request.POST['tipo_doc_identidad'],
                nro_doc_identidad = request.POST['nro_doc_identidad'],
                organizacion = request.POST['organizacion'],
                distrito = request.POST['distrito'],
                tipo_observacion = request.POST['tipo_observacion'],
                documento_observacion = request.POST['documento_observacion'],
                observaciones =request.POST['observaciones'],
                archivo_adjunto = request.FILES['archivo_adjunto'],

            )
            #guardamos la instancia en la base de datos
            newConsulta.save()

            #redireccionamos a la pagina del Formulario de Consulta Publica
            return redirect('consulta_form')
        else:
            message = "The Form in not Valid !, Fix it, o te pego"

    else:
        miFormulario = ConsultaForm()


    context = {
        "title": "Consulta Pública",
        "message": message,
        "form": miFormulario
    }        


    return render(request,"consulta/consulta_form.html", context)



def EnviarEmail(request):

    if request.method=='POST':
        
        #
        return render(request, "consulta/gracias.html")    
    

    return render(request, "consulta/enviaremail.html")    


def my_view(request):
    print('Hi ZhypeR')    

    message = 'Upload many Files !!'

    if request.method=='POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(direccion=request.POST['direccion'],docfile=request.FILES['docfile'])
            newdoc.save()
            # redirect to List !!
            return redirect("my-view")
        else:
            message = "The Form in not Valid !, Fix it, o te pego"
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    context = {
        "documents": documents,
        "form": form,
        "message": message
    }

    return render(request, "consulta/lista_documents.html", context)


class ZonasApiView(APIView):
    def get(self, request):
        zonas = TZona.objects.all()
        serializer = ZonaSerializer(zonas, many=True)
        return Response(serializer.data)

class ZonaByCodigoApiView(APIView):
    def get(self, request, codigozona):
        zonas = TZona.objects.all().filter(codigo_zona=codigozona)
        serializer = ZonaSerializer(zonas, many=True)
        return Response(serializer.data)


class PlanApiView(APIView):
    def get(self, request):
        planes = Plan.objects.all()
        serializer = PlanSerializer(planes, many=True)
        return Response(serializer.data)

"""API: List All Planes Full Detail"""
class PlanFullApiView(APIView):
    def get(self, request):
        planes = Plan.objects.all()
        serializer = PlanFullSerializer(planes, many=True)
        return Response(serializer.data)        

"""API: List All Planes Full Detail by Codigo Zona"""
class PlanFullByCodigoZonaApiView(APIView):
    def get(self,request,codigozona):
        #planes = Plan.objects.all().filter(zona__codigo_zona=codigozona)
        planes = Plan.objects.all().filter(nombre__contains=codigozona)
        serializer = PlanFullSerializer(planes, many=True)
        return Response(serializer.data)


"""API: List All Parametros Urbanos PDU"""
class ParametrosUrbanosApiView(APIView):
    def get(self, request):
        parametros = ParametroUrbanoPDU.objects.all()
        serializer = ParametroUrbanoSerializer(parametros, many=True)
        return Response(serializer.data)


class ParametroUrbanoByCodigoApiView(APIView):
    def get(self, request, codzona):
        parametros = ParametroUrbanoPDU.objects.filter(cod_zona=codzona).first()
        serializer = ParametroUrbanoSerializer(parametros, many=False)
        return Response(serializer.data)

"""NO API views"""

def stats(request):
    views = (
        ViewGraph.objects.all()
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )
    view_s =json.dumps(list(views), cls=DjangoJSONEncoder)

    return render(request, "zonas/stats.html",{
        'view_s': view_s
    })


# Creating views
class EditorChartView(TemplateView):
    template_name = 'zonas/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        return context    

class PoblacionZonaByCodigoZonaApiView(APIView):
    def get(self, request, codzona):
        poblacion = ZonaPoblacion.objects.all().filter(codigo_zona=codzona)
        serializer = PoblacionZonaSerializer(poblacion, many=True)
        return Response(serializer.data)




"""HOME ZONAS"""
#--------------------------------------------------------------------------------------------------------

def HomeZonaMain(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    #zona_presentacion = ZonaPresentacion.objects.get(codigo_zona=codigozona)

    zona_gis = GisBaseZonasZreV2.objects.all().filter(codigo_zre=codigozona)
    zona_vertices_gis = GisBaseZonasZreVertices.objects.all().filter(codigo_zre=codigozona).order_by('etiqueta')
    zona_ambito_vertices_gis = GisBaseZonasAmbitosVertices.objects.all().filter(codigo_zre=codigozona).order_by('etiqueta')

    try:
        zona_presentacion = ZonaPresentacion.objects.get(codigo_zona=codigozona)
        print(zona_presentacion)
    except ZonaPresentacion.DoesNotExist:
        zona_presentacion = None
    
    plan = Plan.objects.get(zona=zona)


    # Metadata OpenGraph----------------------------------------------------------------------------------
    og_title = "Zona de Reglamentacion Especial - " + zona.codigo_zona
    og_description = "Proyecto 41ZRE | Sub Gerencia de Ordenamiento Territorial Provincial | Municipalidad Provincial del Cusco"
    og_image = "http://sgot.cusco.gob.pe:90/zre41media/documents/"+zona.codigo_zona+"/"+zona.codigo_zona+"_ZONIFICACION.jpg"
    
    context = {
        "title": "Zona de Reglamentación Especial : "+zona.codigo_zona,
        "zona": zona,
        "zona_gis": zona_gis,
        "zona_vertices_gis": zona_vertices_gis,
        "zona_ambito_vertices_gis": zona_ambito_vertices_gis,
        "zona_presentacion": zona_presentacion,
        "plan": plan,
        #og
        "og_title": og_title,
        "og_description": og_description,
        "og_image": og_image,
    }
    return render(request,'zonas/homeZona_Main.html', context)



#--------------------------------------------------------------------------------------------------------
def HomeZonaMapas(request,codigozona,etapaplan=None):

    mapas = None
    etapas_metadata = []

    zona = TZona.objects.get(codigo_zona=codigozona)

    plan = Plan.objects.get(zona=zona)

    if etapaplan != None:
        # etapas = get_object_or_404(PlanMapa,plan_etapa=etapaplan)
        mapaslist = PlanMapa.objects.all().filter(plan=plan,plan_etapa__slug=etapaplan)
        # print(mapaslist)
        # PAGINACION --------------------------------------------------------------------------------------------------------
        page = request.GET.get('page')
        paginator = Paginator(mapaslist, 12)
        try:
            mapaslist_paginated = paginator.page(page)
        except PageNotAnInteger:
            mapaslist_paginated = paginator.page(1)
        except EmptyPage:
            mapaslist_paginated = paginator.page(paginator.num_pages)
        # PAGINACION --------------------------------------------------------------------------------------------------------
    else:
        mapaslist = PlanMapa.objects.all().filter(plan=plan)
        # print(mapaslist)
        # PAGINACION --------------------------------------------------------------------------------------------------------
        page = request.GET.get('page')
        paginator = Paginator(mapaslist, 12)
        try:
            mapaslist_paginated = paginator.page(page)
        except PageNotAnInteger:
            mapaslist_paginated = paginator.page(1)
        except EmptyPage:
            mapaslist_paginated = paginator.page(paginator.num_pages)
        # PAGINACION --------------------------------------------------------------------------------------------------------
            


    """recorriendo los mapas"""
    """Obteniendo las distintas Etapas de un determinado Plan"""
    etapas = PlanMapa.objects.all().filter(plan=plan).distinct('plan_etapa')

    for i in etapas:
        print(i.plan_etapa)

    """Obteniendo las distintas Etapas y sus respectiva Cantidad de mapas de un determinado Plan"""
    mapas_plan =  PlanMapa.objects.filter(plan=plan).values('plan_etapa','plan_etapa__slug','plan_etapa__nombre').annotate(Count('plan_etapa'))
    print(mapas_plan)
    """fin"""

    mapas_plan_all =  PlanMapa.objects.filter(plan=plan)

    websitename = WebsiteName.objects.get(id=1)

    zonas = TZona.objects.all()

    #--------------------------------------------------------------------------------------

    mapascaracterizacion = PlanMapa.objects.filter(plan=plan, plan_etapa__nombre='Caracterización')

    mapascaracterizacion_count = mapascaracterizacion.count()

    mapaspropuesta = PlanMapa.objects.filter(plan=plan, plan_etapa__nombre='Propuesta')

    mapaspropuesta_count = mapaspropuesta.count()

    #--------------------------------------------------------------------------------------

    """Datos Estadisticos"""

    #POBLACION----------------------------------------------------------------------------------------
    poblacion = ZonaPoblacion.objects.all().filter(codigo_zona=codigozona)
    poblacion_tabla = ZonaPoblacionTabla.objects.all().filter(codigo_zona=codigozona).order_by('rango')
    poblacion_tabla_total=ZonaPoblacionTabla.objects.filter(codigo_zona=codigozona).aggregate(total=Sum('valor'))['total'] 


    #NIVEL INSTRUCCION--------------------------------------------------------------------------------
    nivel_instruccion_tabla = ZonaNivelInstruccionTabla.objects.all().filter(codigo_zona=codigozona)

    #DENSIDAD POBLACIONAL-----------------------------------------------------------------------------
    densidad_poblacional_tabla = ZonaDensidadPoblacionalTabla.objects.all().filter(codigo_zona=codigozona)

    # Metadata OpenGraph----------------------------------------------------------------------------------
    og_title = "Zona de Reglamentacion Especial - " + zona.codigo_zona
    og_description = "Proyecto 41ZRE | Sub Gerencia de Ordenamiento Territorial Provincial | Municipalidad Provincial del Cusco"
    og_image = "http://sgot.cusco.gob.pe:90/zre41media/documents/"+zona.codigo_zona+"/"+zona.codigo_zona+"_ZONIFICACION.jpg"
    
    context = {
        "title": "Zona: "+codigozona,
        "WebsiteName": websitename,
        'zona': zona,
        'zonas': zonas,
        'mapaslist': mapaslist_paginated,
        'mapaslist_count': mapaslist.count(),
        'mapas_plan': mapas_plan,
        'mapas_plan_all': mapas_plan_all,
        
        "plan": plan,
        "mapasCaracterizacion": mapascaracterizacion,
        "mapascaracterizacion_count": mapascaracterizacion_count,
        "mapasPropuesta": mapaspropuesta,
        "mapaspropuesta_count": mapaspropuesta_count,

        #poblacion
        "poblacion": poblacion,
        "poblacion_tabla": poblacion_tabla,
        "poblacion_tabla_total": poblacion_tabla_total,
        
        #nivel_instruccion
        "nivel_instruccion_tabla": nivel_instruccion_tabla,    

        #densidad_poblacional
        "densidad_poblacional_tabla": densidad_poblacional_tabla,

        #og
        "og_title": og_title,
        "og_description": og_description,
        "og_image": og_image,

    }
    return render(request, 'zonas/homeZona_Mapas.html', context)



def Home41ZRE(request):
    context = {
        "title": "Zona: CUSCO",
    }
    return render(request,'zonas/home41ZRE.html', context)







"""ZONA TEMPLATE LOCAL"""


def HomeZonaLocal(request):
    context = {
        "title" : "Local Template"
    }
    return render(request, "zonas2/home.html", context )

#Capitulo I---------------------------------------------------------------------------------------------------------------------

def HomeZonaConsideraGenerales(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_consideraciones_generales = ZonaConsideracionesGenerales.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_consideraciones_generales": zona_consideraciones_generales,
    }
    return render(request,'zonas/homeZona_c1_ConsideracionesGenerales.html', context)


def HomeZonaObjetivos(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_objetivos = ZonaObjetivos.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_objetivos": zona_objetivos,
    }
    return render(request,'zonas/homeZona_c1_Objetivos.html', context)

def HomeZonaJustificacion(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_justificacion = ZonaJustificacion.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_justificacion": zona_justificacion,
    }
    return render(request,'zonas/homeZona_c1_Justificacion.html', context)

def HomeZonaMetodogia(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_metodologia = ZonaMetodologia.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_metodologia": zona_metodologia
    }
    return render(request,'zonas/homeZona_c1_Metodologia.html', context)

def HomeZonaDelimitacion(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_delimitacion = ZonaDelimitacion.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_delimitacion": zona_delimitacion
    }
    return render(request,'zonas/homeZona_c1_Delimitacion.html', context)

def HomeZonaPlaneamiento(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    zona_planeamiento = ZonaPlaneamiento.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "zona_planeamiento": zona_planeamiento
    }
    return render(request,'zonas/homeZona_c1_Planeamiento.html', context)

#Capitulo II---------------------------------------------------------------------------------------------------------------------


def HomeZonaCaracterizacionSocioeconomica(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    caracterizacion_socioeconomica = ZonaCaracterizacionSocioeconomica.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "caracterizacion_socioeconomica": caracterizacion_socioeconomica
    }
    return render(request,'zonas/homeZona_c2_CaracterizacionSocioeconomica.html', context)

def HomeZonaCaracterizacionLegal(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    caracterizacion_legal = ZonaCaracterizacionLegal.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "caracterizacion_legal": caracterizacion_legal
    }
    return render(request,'zonas/homeZona_c2_CaracterizacionLegal.html', context)

def HomeZonaCaracterizacionGRDDeterminacionPeligro(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    caracterizacion_grd_determinacion_peligro = ZonaCaracterizacionGRDDeterminacionPeligro.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "caracterizacion_grd_determinacion_peligro": caracterizacion_grd_determinacion_peligro
    }
    return render(request,'zonas/homeZona_c2_CaracterizacionGRDDeterminacionPeligro.html', context)

def HomeZonaCaracterizacionGRDAnalisisVulnerabilidad(request,codigozona,etapaplan=None):
    zona = TZona.objects.get(codigo_zona=codigozona)
    caracterizacion_grd_analisis_vulnerabilidad = ZonaCaracterizacionGRDAnalisisVulnerabilidad.objects.get(codigo_zona=codigozona)
    context = {
        "title": "Zona: CUSCO",
        "zona": zona,
        "caracterizacion_grd_analisis_vulnerabilidad": caracterizacion_grd_analisis_vulnerabilidad
    }
    return render(request,'zonas/homeZona_c2_CaracterizacionGRDAnalisisVulnerabilidad.html', context)