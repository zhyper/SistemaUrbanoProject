from django.urls import path, include

from .views import Home41ZRE, HomeZonaCaracterizacionGRDAnalisisVulnerabilidad, HomeZonaCaracterizacionGRDDeterminacionPeligro, HomeZonaCaracterizacionLegal, HomeZonaCaracterizacionSocioeconomica, HomeZonaDelimitacion, HomeZonaJustificacion, HomeZonaMapas, HomeZonaConsideraGenerales, HomeZonaMain, HomeZonaMetodogia, HomeZonaObjetivos, HomeZonaPlaneamiento, ScrollyTellingMapbox
from .views import HomeGeodataAreasPeligroMuyAlto, HomeGeodataAreasConservacionProteccionAmbiental
from .views import ConsultaWebPlan, EditorChartView,EnviarEmail,my_view, ZonaByCodigoApiView
from .views import stats, HomeZonaLocal

#from django.views.generic import TemplateView



urlpatterns = [

    path('', Home41ZRE, name='home_zona' ),
    path('listadocumentos/', my_view, name="my-view"),
    path('stats/', stats, name="view_stats"),
    path('chart/', EditorChartView.as_view(), name="view_chart"),
    path('formularioconsulta/', ConsultaWebPlan, name='consulta_form'),
    path('formularioenviaremail/', EnviarEmail , name='enviar_email'),
    path('zonas/', HomeZonaLocal, name='home_zona_local'),
    #geodata
    path('geodata/apma',HomeGeodataAreasPeligroMuyAlto, name="home_geodata_areas_peligro_muy_alto"),
    path('geodata/acpa',HomeGeodataAreasConservacionProteccionAmbiental, name="home_geodata_areas_conservacion_proteccion_ambiental"),
    
    path('codzona/<str:codigozona>', ZonaByCodigoApiView.as_view(), name='zonas_list_by_codzona'),   
    
    path('<str:codigozona>/', HomeZonaMain, name='zona_by_codigo' ),
    #capitulo I
    path('<str:codigozona>/consideraciones-generales/', HomeZonaConsideraGenerales, name='zona_consideraciones_generales' ),
    path('<str:codigozona>/objetivos/', HomeZonaObjetivos, name='zona_objetivos' ),
    path('<str:codigozona>/justificacion/', HomeZonaJustificacion, name='zona_justificacion' ),
    path('<str:codigozona>/metodologia/', HomeZonaMetodogia, name='zona_metodologia' ),
    path('<str:codigozona>/delimitacion/', HomeZonaDelimitacion, name='zona_delimitacion' ),
    path('<str:codigozona>/planeamiento/', HomeZonaPlaneamiento, name='zona_planeamiento' ),

    #capitulo II
    #SOCIOECONOMICA
    path('<str:codigozona>/caracterizacion-socioeconomica/', HomeZonaCaracterizacionSocioeconomica, name='zona_caracterizacion_socioeconomica' ),
    #LEGAL
    path('<str:codigozona>/caracterizacion-legal/', HomeZonaCaracterizacionLegal, name='zona_caracterizacion_legal' ),
    # GRD
    path('<str:codigozona>/determinacion-del-peligro/', HomeZonaCaracterizacionGRDDeterminacionPeligro, name='zona_determinacion_peligro' ),
    path('<str:codigozona>/analisis-de-vulnerabilidad/', HomeZonaCaracterizacionGRDAnalisisVulnerabilidad, name='zona_analisis_vulnerabilidad' ),
    path('<str:codigozona>/calculo-de-niveles-riesgo/', HomeZonaCaracterizacionGRDAnalisisVulnerabilidad, name='zona_calculo_niveles_riesgo' ),
    path('<str:codigozona>/calculo-perdidas/', HomeZonaCaracterizacionGRDAnalisisVulnerabilidad, name='zona_calculo_perdidas' ),
    path('<str:codigozona>/control-riesgo/', HomeZonaCaracterizacionGRDAnalisisVulnerabilidad, name='zona_control_riesgo' ),
    

    path('<str:codigozona>/mapas/', HomeZonaMapas, name='zona_by_codigo_by_etapa' ),
    path('<str:codigozona>/mapas/<str:etapaplan>', HomeZonaMapas, name='zona_by_codigo_by_etapa' ),

    path('iframe/scrollytelling', ScrollyTellingMapbox.as_view(), name='scrollytelling'),
    


]
