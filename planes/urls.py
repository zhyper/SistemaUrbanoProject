from django.urls import include, path
from .views import HomePlanes,HomePlan,HomeMapasWeb
#from world.views import SourceWMSHome, Home


urlpatterns = [
    path('',HomePlanes, name='home_planes'),
    path('mapas/',HomeMapasWeb, name='home_mapas_web'),
    path('<str:planslug>/',HomePlan, name='home_plan'),
    path('<str:planslug>/<str:etapaplan>',HomePlan, name='plan_by_etapa'),

]