from django.urls import include, path
from . import views
#from world.views import SourceWMSHome, Home
# from planes import urls
# from zonas import urls


urlpatterns = [
    path('',views.Home, name='Home'),
    path('wms',views.SourceWMSHome, name='Wms'),
    path('categoriaEdad/<int:edad>', views.categoriaEdad, name='CatEdad'),
    path('wmsTemplate', views.WmsPlantilla),
    path('mapok',views.MapOk, name='map-ok'),
    path('mapok2',views.MapOk2, name='map-ok-2'),
    path('tikarymap', views.TikaryMap, name='tikary_map'),
    path('zonas/', include('zonas.urls')),
    #path('homezona/<str:codigozona>', views.HomeZonas, name='home_zona'),
    path('planes/', include('planes.urls')),
     
    
]



