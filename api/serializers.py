
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from planes.models import ParametroUrbanoPDU
from zonas.models import Componente, GisLoteCentroidePoints, Plan, PlanEtapa, PlanMapa, Proyecto, TZona
from zonas.models import ZonaPoblacion

class PlanSerializer (serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class ZonaSerializer (serializers.ModelSerializer):
    planes = PlanSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = TZona
        fields = ('codigo_zona','nombre','image','distrito','lat','lng','zoom','observacion','planes')


class PlanEtapaSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = PlanEtapa
        fields = '__all__'        

class ProyectoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ComponenteSerializer (serializers.ModelSerializer):
    proyecto = ProyectoSerializer(
        #many=True,
        read_only=True,
    )

    class Meta:
        model = Componente
        fields = '__all__'

class MapasSerializer (serializers.ModelSerializer):
    plan_etapa = PlanEtapaSerializer()
    
    componente = ComponenteSerializer()

    class Meta:
        model = PlanMapa
        fields = ('nombre','codigo','url','componente','plan','plan_etapa','mapa_tipo_id','planEtapa_id')


"""PLan API"""
class PlanFullSerializer (serializers.ModelSerializer):
    zona = ZonaSerializer(
        #many=True,
        read_only=True,
    )

    mapas = MapasSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Plan
        fields = ('nombre','image','zona','mapas')



"""Parametros urbanos PDU"""

class ParametroUrbanoSerializer (serializers.ModelSerializer):
    class Meta:
        model = ParametroUrbanoPDU
        fields = '__all__'


"""Poblacion Zona API"""

class PoblacionZonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = ZonaPoblacion
        # fields = '__all__'
        fields = ('ge_0_5','ge_6_12','ge_13_18','ge_19_30','ge_31_54','ge_55_65','ge_66_mas')


""" Lotes API """
class GisLoteCentroidePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GisLoteCentroidePoints
        fields = ('lat','lng','poblacion')