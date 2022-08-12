from django.contrib import admin

from planes.models import MapaWeb

# Register your models here.

admin.site.register(MapaWeb, admin.ModelAdmin)