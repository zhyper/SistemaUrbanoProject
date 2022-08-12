from django.contrib import admin

from .models import Slide, SlideItem, WebsiteName

# Register your models here.

class SlideItemAdmin(admin.ModelAdmin):
    list_display = ('nombre','titulo','slide',)

class WebsiteNameAdmin(admin.ModelAdmin):
    list_display = ('nombre_website','ip_production','ip_development',)



admin.site.register(Slide, admin.ModelAdmin)
#admin.site.register(SlideItem, admin.ModelAdmin)
admin.site.register(SlideItem, SlideItemAdmin)
admin.site.register(WebsiteName, WebsiteNameAdmin)



