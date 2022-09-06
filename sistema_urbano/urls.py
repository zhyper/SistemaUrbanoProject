"""Visualizator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.gis import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from api import urls as api_urls


admin.site.site_header = 'Sistema Urbano PM41ZRE Administración'
admin.site.site_title = 'Sistema Urbano PM41ZRE Administración'

#from world import views

urlpatterns = [
    path('',include('world.urls')),
    path('auth/', include('auth_sys_urbano.urls')),
    path('admin/', admin.site.urls),
    #path('tinymce/', include('tinymce.urls')),
    #path('froala_editor/',include('froala_editor.urls'))
    path('summernote/', include('django_summernote.urls')),
    path('api/', include(api_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)