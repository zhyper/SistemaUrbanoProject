from unittest import mock
from django.contrib import admin
from .models import Editors, Plan,PlanMapa, ZonaCaracterizacionLegal, ZonaCaracterizacionSocioeconomica,  ZonaConsideracionesGenerales, ZonaDelimitacion, ZonaDensidadPoblacionalTabla, ZonaJustificacion, ZonaMetodologia, ZonaNivelInstruccionTabla, ZonaObjetivos, ZonaPlaneamiento, ZonaPoblacion, ZonaPoblacionTabla, ZonaPresentacion, Zony2

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','prioridad','url_documento','url_reglamento')
    search_fields = ['nombre']


class ZonaPoblacionTablaAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_zona','rango','valor')
    list_display_links = ('codigo_zona',)
    search_fields = ['codigo_zona']


class ZonaDensidadPoblacionalTablaAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_zona','aoi','tipo_densidad','valor')
    list_display_links = ('codigo_zona',)
    search_fields = ['codigo_zona']

class ZonaNivelInstruccionTablaAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_zona','rango','valor')
    list_display_links = ('codigo_zona',)
    search_fields = ['codigo_zona']


admin.site.register(Zony2, admin.ModelAdmin)
    
admin.site.register(Plan, PlanAdmin)

admin.site.register(ZonaPoblacion, admin.ModelAdmin)

admin.site.register(ZonaPoblacionTabla, ZonaPoblacionTablaAdmin)

admin.site.register(ZonaNivelInstruccionTabla, ZonaNivelInstruccionTablaAdmin)

admin.site.register(Editors, admin.ModelAdmin)

admin.site.register(ZonaDensidadPoblacionalTabla,ZonaDensidadPoblacionalTablaAdmin)

class PlanMapaAdmin(admin.ModelAdmin):
    list_display = ('nombre','plan','plan_etapa')
    # list_display_links = ('codigo_zona',)
    search_fields = ['plan__nombre']


admin.site.register(PlanMapa, PlanMapaAdmin)


# CAPITULO I---------------------------------------------------------------------------------------
class ZonaPresentacionAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)


class ZonaConsideracionesGeneralesAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

class ZonaObjetivosAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

class ZonaJustificacionAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

class ZonaMetodologiaAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)

class ZonaDelimitacionAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

class ZonaPlaneamientoAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

admin.site.register(ZonaPresentacion, ZonaPresentacionAdmin)

admin.site.register(ZonaConsideracionesGenerales, ZonaConsideracionesGeneralesAdmin)

admin.site.register(ZonaObjetivos, ZonaObjetivosAdmin)

admin.site.register(ZonaJustificacion, ZonaJustificacionAdmin)

admin.site.register(ZonaMetodologia, ZonaMetodologiaAdmin)

admin.site.register(ZonaDelimitacion, ZonaDelimitacionAdmin)

admin.site.register(ZonaPlaneamiento, ZonaPlaneamientoAdmin)

# CAPITULO II---------------------------------------------------------------------------------------
class ZonaCaracterizacionSocioeconomicaAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)

class ZonaCaracterizacionLegalAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)    

admin.site.register(ZonaCaracterizacionSocioeconomica, ZonaCaracterizacionSocioeconomicaAdmin)    
admin.site.register(ZonaCaracterizacionLegal, ZonaCaracterizacionLegalAdmin)
