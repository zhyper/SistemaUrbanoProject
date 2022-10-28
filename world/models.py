#from django.db import models

from django.contrib.gis.db import models



# Create your models here.


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name
    
class SourceWMS(models.Model):
    name = models.CharField('Nombre',max_length=255)
    visible =  models.BooleanField('Visibilidad')
    title= models.CharField('Titulo',max_length=255, null=True)
    
    def __str__(self):
        return self.name

class GisBaseZonasZre(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    codigo_zona = models.CharField(max_length=255, blank=True, null=True)
    #mpoly = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    mpoly = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    def __str__(self):
        return self.codigo_zona

    class Meta:
        #managed = False
        db_table = 'gis_base_zonas_zre'    


class GisBaseZonasZreDjango(models.Model):
    id = models.IntegerField(primary_key=True)
    #geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    geom = models.MultiPolygonField(srid=32719)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.codigo

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_zre_django'        

class Comarca(models.Model):
    admapkey = models.BigIntegerField()
    geom = models.MultiPolygonField()        

    def __str__(self):
        return self.admapkey

class Ambitos(models.Model):
    objectid = models.BigIntegerField()
    admapkey = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField()        

    def __str__(self):
        return str(self.admapkey)

class Ambitosutm(models.Model):
    objectid = models.BigIntegerField()
    admapkey = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=32719)  

    def __str__(self):
        return str(self.admapkey)      

TIPO_ZRE_CHOICES = [
    ('apma','Areas de Peligro Muy Alto'),
    ('acpa','Areas de Conservación y Protección Ambiental'),
]

class TZona(models.Model):
    #id = models.IntegerField(primary_key=True)
    codigo_zona = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)
    distrito = models.CharField(max_length=50, null=True)
    lat = models.DecimalField(decimal_places=10, max_digits=20, null=True)
    lng = models.DecimalField(decimal_places=10, max_digits=20, null=True)
    zoom = models.DecimalField(decimal_places=10, max_digits=20, null=True)
    observacion = models.TextField(null=True)
    tipo_zre = models.CharField(max_length=15,null=True, choices=TIPO_ZRE_CHOICES)
    pitch = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    bearing = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=6, null=True)

    class Meta:
        managed = True
        db_table = 't_zona'  
    
    def __str__(self):
        return str(self.codigo_zona)      