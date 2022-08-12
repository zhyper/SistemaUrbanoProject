from django.db import models

# Create your models here.
class ParametroUrbanoPDU(models.Model):

    tipo_area = models.CharField(max_length=100)
    cod_tipo_area= models.CharField(max_length=100)
    tipo_zona= models.CharField(max_length=100)
    cod_tipo_zona= models.CharField(max_length=100)
    zona= models.CharField(max_length=100)
    cod_zona= models.CharField(max_length=100)
    usos= models.CharField(max_length=100)
    densidad_neta= models.IntegerField()
    lote_minimo= models.IntegerField()
    frente_minimo= models.IntegerField()
    altura_edifica = models.CharField(max_length=100)
    coeficiente_edifica = models.DecimalField(max_digits=10, decimal_places=2)
    area_edifica= models.IntegerField()
    area_libre= models.IntegerField()
    estacionamiento = models.CharField(max_length=100)
    nivel_servicio = models.CharField(max_length=100)
    lote_frente_minimo = models.CharField(max_length=100)
    residencial_compatible = models.CharField(max_length=100)
    agno_aprobacion = models.CharField(max_length=100)

    def __str__(self):
        return self.cod_zona    

    class Meta:
        managed = False
        db_table = 't_parametro_urbano_pdu'
        verbose_name = 'Parametro PDU'
        verbose_name_plural = 'Parametros PDU'

class MapaWeb(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre    

    class Meta:
        managed = True
        db_table = 't_mapa_web'
        verbose_name = 'Mapa Web'
        verbose_name_plural = 'Mapas Web'