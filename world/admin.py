from django.contrib.gis import admin
from .models import Ambitos, Ambitosutm, SourceWMS, TZona, WorldBorder, GisBaseZonasZre, GisBaseZonasZreDjango

# Register your models here.
admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(GisBaseZonasZre, admin.GeoModelAdmin)
admin.site.register(SourceWMS, admin.ModelAdmin)
admin.site.register(GisBaseZonasZreDjango, admin.GeoModelAdmin)
admin.site.register(Ambitos, admin.GeoModelAdmin)
admin.site.register(Ambitosutm, admin.GeoModelAdmin)
admin.site.register(TZona,admin.ModelAdmin)
