from django.db import models

# Create your models here.


class WebsiteName(models.Model):
    nombre_website = models.CharField(max_length=200)
    ip_production = models.CharField(max_length=100)
    ip_development = models.CharField(max_length=100)
    dominio = models.CharField(max_length=100, default='', null=True)

    class Meta:
        #managed = True
        db_table = 't_website_name' 

    def __str__(self):
        return self.nombre_website


class Slide(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 't_web_slide' 

    def __str__(self):
        return self.nombre



class SlideItem(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    # slide = models.ForeignKey(Slide, on_delete = models.CASCADE, related_name='slides')
    slide = models.ForeignKey(Slide, on_delete = models.CASCADE)

    class Meta:
        managed = False
        db_table = 't_web_slide_item' 

    def __str__(self):
        return self.nombre

    
