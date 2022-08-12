from multiprocessing import context
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from requests import request
from django.db.models import Count
from planes.models import MapaWeb


from zonas.models import Plan, PlanMapa
from portal.models import WebsiteName

# Create your views here.

def HomePlanes(request):

    """Listar solo los Planes Aprobados (estado_plan_id = 2)"""
    planes_aprobados = Plan.objects.all().filter(estado_plan_id=2)

    # Metadata OpenGraph----------------------------------------------------------------------------------
    og_title = "Planes Territoriales | Plataforma de Gestión Territorial Provincial Cusco"
    og_description = "Municipalidad Provincial del Cusco"
    og_image = "http://sgot.cusco.gob.pe:90/zre41media/slides/home/banner_planes_1200.jpg"

    context = {
        "title": "Plataforma de Gestión Territorial | SGOTP | 2022",
        "planes_aprobados": planes_aprobados,
        #og
        "og_title": og_title,
        "og_description": og_description,
        "og_image": og_image,
    }

    return render(request,"planes/homePlanes.html", context)


def HomePlan(request,planslug,etapaplan=None):

    plan = Plan.objects.get(slug=planslug)

    if etapaplan != None:
        mapaslist = PlanMapa.objects.all().filter(plan=plan, plan_etapa__slug=etapaplan)
        #PAGINACION--------------------------------------------------------------------------------------------------
        page = request.GET.get('page')
        paginator = Paginator(mapaslist,12)
        try:
            mapaslist_paginated = paginator.page(page)
        except PageNotAnInteger:
            mapaslist_paginated = paginator.page(1)
        except EmptyPage:
            mapaslist_paginated = paginator.page(paginator.num_pages)

    else:
        mapaslist = PlanMapa.objects.all().filter(plan=plan)
        #PAGINATION----------------------------------------------------------------------------------------------------
        page = request.GET.get('page')
        paginator = Paginator(mapaslist,12)
        try:
            mapaslist_paginated = paginator.page(page)
        except PageNotAnInteger:
            mapaslist_paginated = paginator.page(1)
        except EmptyPage:
            mapaslist_paginated = paginator.page(paginator.num_pages)
        



    """Obteniendo las distintas Etapas y sus respectiva Cantidad de mapas de un determinado Plan"""
    mapas_plan =  PlanMapa.objects.filter(plan=plan).values('plan_etapa','plan_etapa__slug','plan_etapa__nombre').annotate(Count('plan_etapa'))
    print(mapas_plan)
    """fin"""

    mapas_plan_all =  PlanMapa.objects.filter(plan=plan)

    # Metadata OpenGraph----------------------------------------------------------------------------------
    og_title = plan.nombre
    og_description = "Proyecto 41ZRE | Sub Gerencia de Ordenamiento Territorial Provincial | Municipalidad Provincial del Cusco"
    og_image = "http://sgot.cusco.gob.pe:90/zre41media/documents/"+plan.codigo_plan+"/"+plan.codigo_plan+".jpg"

    context = {
        "title": "Detalle Plan",
        "nombre_plan": planslug,
        "plan": plan,
        "mapaslist": mapaslist_paginated,
        "mapas_plan": mapas_plan,
        "mapas_plan_all": mapas_plan_all,
        #og
        "og_title": og_title,
        "og_description": og_description,
        "og_image": og_image,
    }

    return render(request,"planes/detalle_plan.html", context)    

def HomeMapasWeb(request):

    """Listar los Mapas Web """
    mapas_web = MapaWeb.objects.all()

    websitename = WebsiteName.objects.get(id=1)

    context = {
        "title": "Plataforma de Gestión Territorial | SGOTP | 2022",
        "mapasweb": mapas_web,
        "WebsiteName": websitename,
    }

    return render(request,"mapas/homeMapas.html", context)    