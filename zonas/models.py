import datetime
from tabnanny import verbose
from wsgiref.validate import validator
from django.utils import timezone
from django.db import models
from world.models import TZona
#from tinymce.models import HTMLField

# Create your models here.


class Zony(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

class Zony2(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        db_table = 'zre41"."zony2'   


class Plan(models.Model):      
    nombre = models.CharField(max_length=200,blank=True, null=True)
    estado = models.CharField(max_length=200,blank=True, null=True)
    image = models.CharField(max_length=200,blank=True, null=True)
    image2 = models.CharField(max_length=200, blank=True, null=True)
    codigo_plan = models.CharField(max_length=200,blank=True, null=True)
    slug = models.SlugField(null=True, default=None, max_length=250)
    estado_plan_id = models.IntegerField()
    url_documento = models.CharField(max_length=200,blank=True, null=True)
    url_reglamento = models.CharField(max_length=200,blank=True, null=True)
    url_evar_cenepred = models.CharField(max_length=200,blank=True, null=True)
    elaboracion_fecha_inicio = models.CharField(max_length=20,null=True,blank=True)
    elaboracion_fecha_fin = models.CharField(max_length=20,null=True,blank=True)
    consulta_fecha_inicio = models.CharField(max_length=20,null=True,blank=True)
    consulta_fecha_fin = models.CharField(max_length=20,null=True,blank=True)
    lev_observaciones = models.CharField(max_length=20,null=True,blank=True)
    aprobacion_fecha = models.CharField(max_length=20,null=True,blank=True)
    aprobacion_documento = models.CharField(max_length=200,blank=True, null=True)
    prioridad = models.CharField(max_length=200,blank=True, null=True)
    tipo_plan_id = models.IntegerField()
    provincia_id = models.IntegerField()
    zona = models.ForeignKey(TZona,on_delete=models.CASCADE,  related_name='planes',)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 't_plan'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    objetivo = models.TextField()
    unidad_organizacional_id = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 't_proyecto'



class Componente(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    abreviacion = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 't_componente_proyecto'

class PlanEtapa(models.Model):
    nombre = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 't_plan_etapa'


class PlanMapa(models.Model):
    nombre = models.CharField(max_length=250)
    codigo = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    componente = models.ForeignKey(Componente,on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='mapas', null=True)
    plan_etapa = models.ForeignKey(PlanEtapa, on_delete=models.CASCADE, null=True)
    mapa_tipo_id = models.IntegerField()
    planEtapa_id = models.IntegerField()
    fecha_updated = models.DateField(default=datetime.date.today, blank=True)


    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 't_plan_mapa'
    

    """FORMS"""

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    direccion = models.CharField(max_length=100, blank=True, null=True )

    def __str__(self):
        return self.direccion

    class Meta:
        managed = True



class Consulta(models.Model):
    email = models.EmailField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_doc_identidad = models.CharField(max_length=50)
    nro_doc_identidad = models.CharField(max_length=10)
    organizacion = models.CharField(max_length=100)
    distrito = models.CharField(max_length=50)
    tipo_observacion = models.CharField(max_length=20)
    documento_observacion = models.CharField(max_length=20)
    observaciones = models.TextField(max_length=500)
    archivo_adjunto = models.FileField(upload_to='documents/%Y/%m/%d')
    fecha_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

"""TABLAS ESTADISTICAS: VARIABLES : INDICADORES"""        


class ZonaPresentacion(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_presentacion'
        verbose_name_plural = '00:Zona 00:00:Presentacion'

#---------------------------------------------------------------------------------------------------------------------

class ZonaConsideracionesGenerales(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_consideraciones_generales'
        verbose_name_plural = '01:Zona C1:01:Considera Generales'

#---------------------------------------------------------------------------------------------------------------------

class ZonaObjetivos(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_objetivos'
        verbose_name_plural = '03:Zona C1:02:Objetivos'

#---------------------------------------------------------------------------------------------------------------------

class ZonaJustificacion(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_justificacion'
        verbose_name_plural = '04:Zona C1:03:Justificacion'

#---------------------------------------------------------------------------------------------------------------------

class ZonaMetodologia(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_metodologia'
        verbose_name_plural = '05:Zona C1:04:Metodologia'

class ZonaDelimitacion(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_delimitacion'
        verbose_name_plural = '06:Zona C1:05:Delimitacion'

#---------------------------------------------------------------------------------------------------------------------
class ZonaPlaneamiento(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_planeamiento'
        verbose_name_plural = '07:Zona C1:06:Planeamiento'

#CAPITULO II ---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
class ZonaCaracterizacionSocioeconomica(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_caracterizacion_socioeconomica'
        verbose_name_plural = '08:Zona C2:07:Caracterizacion Socioeconomica'
#---------------------------------------------------------------------------------------------------------------------
class ZonaCaracterizacionLegal(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_caracterizacion_legal'
        verbose_name_plural = '09:Zona C2:08:Caracterizacion Legal'
#---------------------------------------------------------------------------------------------------------------------
#GRD
class ZonaCaracterizacionGRDDeterminacionPeligro(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_carac_grd_determ_peligro'
        verbose_name_plural = '10:Zona C2:09:Caracterizacion GRD Determinacion Peligro'


#---------------------------------------------------------------------------------------------------------------------
class ZonaCaracterizacionGRDAnalisisVulnerabilidad(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.codigo_zona
    
    class Meta:
        managed = True 
        db_table = 't_zona_carac_grd_anali_vulnera'
        verbose_name_plural = '11:Zona C2:10:Caracterizacion GRD Analisis Vulnerabilidad'

#---------------------------------------------------------------------------------------------------------------------        


class ZonaPoblacion(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    agno = models.IntegerField(null=True, default=0)
    ge_0_5 = models.IntegerField( null=True, default=0)
    ge_6_12 = models.IntegerField( null=True, default=0)
    ge_13_18 = models.IntegerField( null=True, default=0)
    ge_19_30 = models.IntegerField( null=True, default=0)
    ge_31_54 = models.IntegerField( null=True, default=0)
    ge_55_65 = models.IntegerField( null=True, default=0)
    ge_66_mas = models.IntegerField( null=True, default=0)
    discapacitados = models.IntegerField( null=True, default=0)
    total = models.IntegerField( null=True, default=0)

    def save(self, *args, **kwargs):
        self.total = self.ge_0_5 + self.ge_6_12 + self.ge_13_18 + self.ge_19_30 + self.ge_31_54 + self.ge_55_65 + self.ge_66_mas + self.discapacitados
        super(ZonaPoblacion, self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo_zona

    class Meta:
        managed = True        
        db_table = 't_poblacion_zona'

class ZonaPoblacionTabla(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    agno = models.IntegerField(null=False)
    rango = models.CharField( max_length=50)
    valor = models.IntegerField( null=True, default=0)
    fuente = models.CharField( max_length=50)
    
    def __str__(self):
        return self.codigo_zona

    class Meta:
        managed = True        
        db_table = 't_poblacion_zona_tabla'


class ZonaNivelInstruccionTabla(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    agno = models.IntegerField(null=True, default=0)
    rango = models.CharField( max_length=50)
    valor = models.DecimalField( max_digits=5, decimal_places=2, null=True, default=0)
    fuente = models.CharField( max_length=50)
    
    def __str__(self):
        #return '{} - {}'.format(self.codigo_zona, self.agno)
        return self.codigo_zona

    class Meta:
        managed = True        
        db_table = 't_nivel_instruccion_zona_tabla'


class ZonaDensidadPoblacionalTabla(models.Model):
    codigo_zona = models.CharField(max_length=50, null=True, blank=True)
    agno = models.IntegerField(null=True, default=0)
    aoi = models.CharField(max_length=250,   null=True)
    tipo_densidad = models.CharField( max_length=250,   null=True)
    valor = models.DecimalField( max_digits=5, decimal_places=2, null=True, default=0)
    nro_habitantes = models.IntegerField( null=True, default=0)
    superficie_aoi = models.DecimalField( max_digits=5, decimal_places=2, null=True, default=0)
    fuente = models.CharField( max_length=50)
    
    def __str__(self):
        return self.codigo_zona

    class Meta:
        managed = True        
        db_table = 't_densidad_poblacional_zona'

class ViewGraph(models.Model):
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)






class Editors(models.Model):
    editor_name = models.CharField(max_length=200)
    num_users = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.editor_name, self.num_users) 