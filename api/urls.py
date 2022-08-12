import django


from django.urls import path, include
from zonas.views import ParametroUrbanoByCodigoApiView, ParametrosUrbanosApiView, PlanApiView, PlanFullByCodigoZonaApiView, PoblacionZonaByCodigoZonaApiView,ZonasApiView,PlanFullApiView


urlpatterns = [
    path('planes/', PlanApiView.as_view(), name='planes_list_api'),   
    path('planesfull/', PlanFullApiView.as_view(), name='planesfull_list_api'),   
    path('planesfull/codigozona/<str:codigozona>', PlanFullByCodigoZonaApiView.as_view(), name='planesfull_by_zona_list_api'),   
    path('zonas/', ZonasApiView.as_view(), name='zonas_list_api'),   
    path('parametrospdu/', ParametrosUrbanosApiView.as_view(), name='parametros_pdu_list_api'),   
    path('parametrospdu/<str:codzona>/', ParametroUrbanoByCodigoApiView.as_view(), name='parametros_pdu_list_api'),  
    path('zonas/poblacion/<str:codzona>/', PoblacionZonaByCodigoZonaApiView.as_view(), name='poblacion_zonas_by_codigozona_api'),  

]