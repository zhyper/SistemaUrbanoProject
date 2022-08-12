# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class 2022GisPropFcZonificacion(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=4, blank=True, null=True)
    objectid = models.BigIntegerField(db_column='OBJECTID', blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sub_zona = models.CharField(db_column='SUB_ZONA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shape_length = models.FloatField(db_column='SHAPE_Length', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='SHAPE_Area', blank=True, null=True)  # Field name made lowercase.
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    id_manzana = models.CharField(max_length=50, blank=True, null=True)
    id_agrupacion = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_agrupacion2 = models.CharField(max_length=15, blank=True, null=True)
    zonificacion_b = models.CharField(db_column='zonificacion_B', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripcion_b = models.CharField(db_column='DESCRIPCION_B', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='UBICACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frente_min = models.FloatField(db_column='FRENTE_MIN', blank=True, null=True)  # Field name made lowercase.
    lote_min = models.FloatField(db_column='LOTE_MIN', blank=True, null=True)  # Field name made lowercase.
    coefi_edifi = models.FloatField(db_column='COEFI_EDIFI', blank=True, null=True)  # Field name made lowercase.
    area_libre = models.FloatField(db_column='AREA_LIBRE', blank=True, null=True)  # Field name made lowercase.
    altura = models.CharField(db_column='ALTURA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    densidad = models.FloatField(db_column='DENSIDAD', blank=True, null=True)  # Field name made lowercase.
    plan_referencia = models.CharField(db_column='PLAN_REFERENCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2022_gis_prop_fc_zonificacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GisBaseCurvas(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    layer = models.CharField(max_length=-1, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_curvas'


class GisBaseZonasAmbitosV2(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_ambitos_v2'


class GisBaseZonasAmbitosVertices(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    etiqueta = models.CharField(max_length=15, blank=True, null=True)
    utm_este = models.FloatField(blank=True, null=True)
    utm_norte = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_ambitos_vertices'


class GisBaseZonasZreDjango(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_zre_django'


class GisBaseZonasZreV2(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_zre_v2'


class GisBaseZonasZreVertices(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.FloatField(blank=True, null=True)
    orig_fid = models.BigIntegerField(blank=True, null=True)
    etiqueta = models.CharField(max_length=5, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    utm_este = models.FloatField(blank=True, null=True)
    utm_norte = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_zre_vertices'


class GisBaseZonasZreVerticesTexto(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.BigIntegerField(blank=True, null=True)
    textstring = models.CharField(max_length=254, blank=True, null=True)
    text_size = models.FloatField(blank=True, null=True)
    text_angle = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_base_zonas_zre_vertices_texto'


class GisCaracAmbAreasCriticasAcumulacionRrss(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    tp_rrss = models.CharField(max_length=80, blank=True, null=True)
    rrss_sp = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrit = models.CharField(max_length=80, blank=True, null=True)
    dc_rglm = models.CharField(max_length=80, blank=True, null=True)
    documnt = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.FloatField(blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_areas_criticas_acumulacion_rrss'


class GisCaracAmbAreasMinado(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_areas_minado'


class GisCaracAmbAreasMinadoTipoExplotacion(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_areas_minado_tipo_explotacion'


class GisCaracAmbCoberturaVegetal(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    cobertura_vegetal = models.CharField(max_length=-1, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_cobertura_vegetal'


class GisCaracAmbCoberturaVegetalCg(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    tipo_cober = models.CharField(max_length=80, blank=True, null=True)
    cobert_veg = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_cobertura_vegetal_cg'


class GisCaracAmbConcesionesMineras(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigou = models.CharField(max_length=13, blank=True, null=True)
    concesion = models.CharField(max_length=50, blank=True, null=True)
    tit_conces = models.CharField(max_length=100, blank=True, null=True)
    d_estado = models.CharField(max_length=50, blank=True, null=True)
    carta = models.CharField(max_length=4, blank=True, null=True)
    zona = models.CharField(max_length=2, blank=True, null=True)
    sustancia = models.CharField(max_length=1, blank=True, null=True)
    depa = models.CharField(max_length=64, blank=True, null=True)
    provi = models.CharField(max_length=128, blank=True, null=True)
    distri = models.CharField(max_length=254, blank=True, null=True)
    hasdatum = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    shape_len = models.FloatField(blank=True, null=True)
    fec_denu = models.DateField(blank=True, null=True)
    leyenda = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_concesiones_mineras'


class GisCaracAmbContaminacionAirePuntosRefer(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_aire_puntos_refer'


class GisCaracAmbContaminacionPolygon(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    contourmin = models.FloatField(blank=True, null=True)
    contourmax = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo = models.CharField(max_length=200, blank=True, null=True)
    afectacion = models.CharField(max_length=200, blank=True, null=True)
    subtipo2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_polygon'


class GisCaracAmbContaminacionPolyline(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    contour = models.BigIntegerField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo = models.CharField(max_length=200, blank=True, null=True)
    afectacion = models.CharField(max_length=200, blank=True, null=True)
    subtipo2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_polyline'


class GisCaracAmbContaminacionPuntosMonitoreoAcustico(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    puntos = models.CharField(max_length=254, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    db_dia = models.FloatField(blank=True, null=True)
    db_noche = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo2 = models.CharField(max_length=200, blank=True, null=True)
    afectacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_puntos_monitoreo_acustico'


class GisCaracAmbContaminacionPuntosMonitoreoAire(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    pto = models.FloatField(blank=True, null=True)
    este = models.FloatField(blank=True, null=True)
    norte = models.FloatField(blank=True, null=True)
    altitud = models.FloatField(blank=True, null=True)
    codigo = models.CharField(max_length=254, blank=True, null=True)
    eca = models.CharField(max_length=50, blank=True, null=True)
    pm2_5 = models.FloatField(blank=True, null=True)
    pm10 = models.FloatField(blank=True, null=True)
    co = models.FloatField(blank=True, null=True)
    so2 = models.FloatField(blank=True, null=True)
    no2 = models.FloatField(blank=True, null=True)
    h2s = models.FloatField(blank=True, null=True)
    o3 = models.FloatField(blank=True, null=True)
    hg = models.FloatField(blank=True, null=True)
    benceno = models.FloatField(blank=True, null=True)
    plomo = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo = models.CharField(max_length=200, blank=True, null=True)
    subtipo2 = models.CharField(max_length=200, blank=True, null=True)
    afectacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_puntos_monitoreo_aire'


class GisCaracAmbContaminacionSuelos(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    codigo = models.CharField(max_length=254, blank=True, null=True)
    zona = models.CharField(max_length=254, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    altitud = models.FloatField(blank=True, null=True)
    plata = models.FloatField(blank=True, null=True)
    aluminio = models.FloatField(blank=True, null=True)
    arsenico = models.FloatField(blank=True, null=True)
    bario = models.FloatField(blank=True, null=True)
    berilio = models.FloatField(blank=True, null=True)
    calcio = models.FloatField(blank=True, null=True)
    cadmio = models.FloatField(blank=True, null=True)
    cobalto = models.FloatField(blank=True, null=True)
    cromo = models.FloatField(blank=True, null=True)
    cobre = models.FloatField(blank=True, null=True)
    hierro = models.FloatField(blank=True, null=True)
    potasio = models.FloatField(blank=True, null=True)
    magnesio = models.FloatField(blank=True, null=True)
    manganeso = models.FloatField(blank=True, null=True)
    molibdeno = models.FloatField(blank=True, null=True)
    sodio = models.FloatField(blank=True, null=True)
    niquel = models.FloatField(blank=True, null=True)
    plomo = models.FloatField(blank=True, null=True)
    antimonio = models.FloatField(blank=True, null=True)
    selenio = models.FloatField(blank=True, null=True)
    talio = models.FloatField(blank=True, null=True)
    vanadio = models.FloatField(blank=True, null=True)
    zinc = models.FloatField(blank=True, null=True)
    boro = models.FloatField(blank=True, null=True)
    bismuto = models.FloatField(blank=True, null=True)
    litio = models.FloatField(blank=True, null=True)
    fosforo = models.FloatField(blank=True, null=True)
    silicio = models.FloatField(blank=True, null=True)
    estano = models.FloatField(blank=True, null=True)
    estroncio = models.FloatField(blank=True, null=True)
    titanio = models.FloatField(blank=True, null=True)
    mercurio = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.CharField(max_length=200, blank=True, null=True)
    tolueno = models.FloatField(blank=True, null=True)
    benceno = models.FloatField(blank=True, null=True)
    etilenbenc = models.FloatField(blank=True, null=True)
    xilenos = models.FloatField(blank=True, null=True)
    naftaleno = models.FloatField(blank=True, null=True)
    benzo_a_pi = models.FloatField(blank=True, null=True)
    fraccion_field = models.FloatField(db_column='fraccion_', blank=True, null=True)  # Field renamed because it ended with '_'.
    fraccion1 = models.FloatField(blank=True, null=True)
    fraccion2 = models.FloatField(blank=True, null=True)
    bifenilos_field = models.FloatField(db_column='bifenilos_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tetracloro = models.FloatField(blank=True, null=True)
    tricloroet = models.FloatField(blank=True, null=True)
    arsénico = models.FloatField(blank=True, null=True)
    bario_tota = models.FloatField(blank=True, null=True)
    cromo_tota = models.FloatField(blank=True, null=True)
    cromo_vi = models.FloatField(blank=True, null=True)
    cianuro_li = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_contaminacion_suelos'


class GisCaracAmbDepositosHecesFecales(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    area = models.FloatField(blank=True, null=True)
    zre = models.CharField(max_length=6, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_depositos_heces_fecales'


class GisCaracAmbDiversidadFlora(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    zre = models.CharField(max_length=6, blank=True, null=True)
    diversidad = models.CharField(max_length=50, blank=True, null=True)
    shannon_id = models.CharField(max_length=50, blank=True, null=True)
    leyenda = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_diversidad_flora'


class GisCaracAmbEaan(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    area_m2 = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_eaan'


class GisCaracAmbEen(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    nombre_eco = models.CharField(max_length=80, blank=True, null=True)
    tipo_eco = models.CharField(max_length=80, blank=True, null=True)
    codigo_eco = models.CharField(max_length=80, blank=True, null=True)
    est_conser = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_een'


class GisCaracAmbEspaciosSuelosDegradados(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    descrip = models.CharField(max_length=50, blank=True, null=True)
    simb = models.CharField(max_length=10, blank=True, null=True)
    coor_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)
    area_m2 = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_espacios_suelos_degradados'


class GisCaracAmbFauna(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    especie = models.CharField(max_length=254, blank=True, null=True)
    autor = models.CharField(max_length=254, blank=True, null=True)
    nombre_com = models.CharField(max_length=254, blank=True, null=True)
    origen = models.CharField(max_length=254, blank=True, null=True)
    familia = models.CharField(max_length=254, blank=True, null=True)
    orden = models.CharField(max_length=254, blank=True, null=True)
    clase = models.CharField(max_length=254, blank=True, null=True)
    cites_peru = models.CharField(max_length=254, blank=True, null=True)
    uicn = models.CharField(max_length=254, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    altitud_m = models.FloatField(db_column='altitud__m', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_fauna'


class GisCaracAmbGa(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    tipo_cober = models.CharField(max_length=80, blank=True, null=True)
    cobert_veg = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    codigo = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_ga'


class GisCaracAmbLetrinas(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_letrinas'


class GisCaracAmbManantiales(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    rd = models.CharField(max_length=80, blank=True, null=True)
    vigenci = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    dist = models.CharField(max_length=80, blank=True, null=True)
    uso = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    nmbr_bn = models.CharField(max_length=80, blank=True, null=True)
    razn_sc = models.CharField(max_length=80, blank=True, null=True)
    tp_dc_d = models.CharField(max_length=80, blank=True, null=True)
    num_res = models.CharField(max_length=80, blank=True, null=True)
    desc_rs = models.CharField(max_length=80, blank=True, null=True)
    tip_res = models.CharField(max_length=80, blank=True, null=True)
    proc_dm = models.CharField(max_length=80, blank=True, null=True)
    rspnsbl = models.CharField(max_length=80, blank=True, null=True)
    est_der = models.CharField(max_length=80, blank=True, null=True)
    clas_us = models.CharField(max_length=80, blank=True, null=True)
    tip_uso = models.CharField(max_length=80, blank=True, null=True)
    clas_dr = models.CharField(max_length=80, blank=True, null=True)
    tip_der = models.CharField(max_length=80, blank=True, null=True)
    clas_fu = models.CharField(max_length=80, blank=True, null=True)
    tip_fue = models.CharField(max_length=80, blank=True, null=True)
    nom_fue = models.CharField(max_length=80, blank=True, null=True)
    tp_p_cp = models.CharField(max_length=80, blank=True, null=True)
    alias = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_manantiales'


class GisCaracAmbPuntosQuemaRrss(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    acc_rrs = models.CharField(max_length=80, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    documnt = models.CharField(max_length=80, blank=True, null=True)
    dc_rglm = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_puntos_quema_rrss'


class GisCaracAmbPuntosVertimiento(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    tipo_vert = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    descripcio = models.CharField(max_length=80, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_puntos_vertimiento'


class GisCaracAmbQuebradas(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    text = models.CharField(max_length=254, blank=True, null=True)
    predios = models.CharField(max_length=50, blank=True, null=True)
    predio = models.CharField(max_length=254, blank=True, null=True)
    tipologia = models.CharField(max_length=254, blank=True, null=True)
    sotano = models.FloatField(blank=True, null=True)
    material_d = models.CharField(max_length=254, blank=True, null=True)
    estado_de = models.CharField(max_length=254, blank=True, null=True)
    estado_d_1 = models.CharField(max_length=254, blank=True, null=True)
    agua_consu = models.CharField(max_length=254, blank=True, null=True)
    desague = models.CharField(max_length=254, blank=True, null=True)
    energia_el = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_quebradas'


class GisCaracAmbResiduosSolidosAreaQuemado(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    zre = models.CharField(max_length=6, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_residuos_solidos_area_quemado'


class GisCaracAmbSueloExplotado(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_suelo_explotado'


class GisCaracAmbZonaProteccionAmbiental(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    codigo = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_zona_proteccion_ambiental'


class GisCaracAmbZpaZonaProteccionAmbiental(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=75, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    zre = models.CharField(max_length=5, blank=True, null=True)
    distrito = models.CharField(max_length=15, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    area_m2 = models.FloatField(blank=True, null=True)
    doc_referencia = models.CharField(max_length=5, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_zpa_zona_proteccion_ambiental'


class GisCaracAmbZpceZonasProteccionConservacionEcologica(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    codigo = models.CharField(max_length=80, blank=True, null=True)
    zre = models.CharField(max_length=80, blank=True, null=True)
    distrito = models.CharField(max_length=80, blank=True, null=True)
    documento = models.CharField(max_length=80, blank=True, null=True)
    doc_reglam = models.CharField(max_length=80, blank=True, null=True)
    fuente = models.CharField(max_length=80, blank=True, null=True)
    area_m2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_zpce_zonas_proteccion_conservacion_ecologica'


class GisCaracAmbZpusZonasProductivasUsoSostenible(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nombre = models.CharField(max_length=75, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    zre = models.CharField(max_length=5, blank=True, null=True)
    distrito = models.CharField(max_length=15, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    doc_referencia = models.CharField(max_length=5, blank=True, null=True)
    area_m2 = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=35, blank=True, null=True)
    codigo_tipo = models.CharField(max_length=5, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_amb_zpus_zonas_productivas_uso_sostenible'


class GisCaracFcAgrupacionesInscritasSunarp(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_agrupaciones_inscritas_sunarp'


class GisCaracFcAmbito(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    fid_field = models.IntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    area = models.FloatField(blank=True, null=True)
    perimetro = models.IntegerField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_ambito'


class GisCaracFcAmbitoVertices(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_ambito_vertices'


class GisCaracFcAmbitoVerticesEtiquetas(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.BigIntegerField(blank=True, null=True)
    textstring = models.CharField(max_length=254, blank=True, null=True)
    text_size = models.FloatField(blank=True, null=True)
    text_angle = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_ambito_vertices_etiquetas'


class GisCaracFcBloques1N(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.FloatField(blank=True, null=True)
    featid1 = models.FloatField(blank=True, null=True)
    cod_bloque = models.CharField(max_length=254, blank=True, null=True)
    departamen = models.FloatField(blank=True, null=True)
    provincia = models.FloatField(blank=True, null=True)
    distrito = models.FloatField(blank=True, null=True)
    cod_zre = models.CharField(max_length=254, blank=True, null=True)
    cod_hab_ur = models.CharField(max_length=254, blank=True, null=True)
    ubicación = models.CharField(max_length=254, blank=True, null=True)
    agrupacion = models.CharField(max_length=254, blank=True, null=True)
    mz = models.CharField(max_length=254, blank=True, null=True)
    lote = models.FloatField(blank=True, null=True)
    sub_lote = models.CharField(max_length=254, blank=True, null=True)
    calificaci = models.CharField(max_length=254, blank=True, null=True)
    bloque = models.CharField(max_length=254, blank=True, null=True)
    uso_predom = models.CharField(max_length=254, blank=True, null=True)
    uso_primer = models.CharField(max_length=254, blank=True, null=True)
    uso_detall = models.CharField(max_length=254, blank=True, null=True)
    pisos = models.FloatField(blank=True, null=True)
    unidades_i = models.FloatField(blank=True, null=True)
    con_sotano = models.CharField(max_length=254, blank=True, null=True)
    entretecho = models.CharField(max_length=254, blank=True, null=True)
    modo_const = models.CharField(max_length=254, blank=True, null=True)
    material = models.CharField(max_length=254, blank=True, null=True)
    estado_con = models.CharField(max_length=254, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    admapkey1 = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_bloques_1n'


class GisCaracFcCatastro(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    cod_catast = models.CharField(max_length=-1, blank=True, null=True)
    bloque = models.CharField(max_length=-1, blank=True, null=True)
    piso = models.IntegerField(blank=True, null=True)
    material_d = models.CharField(max_length=-1, blank=True, null=True)
    estado_de = models.CharField(max_length=-1, blank=True, null=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    predios = models.CharField(max_length=-1, blank=True, null=True)
    predio = models.CharField(max_length=-1, blank=True, null=True)
    tipologia = models.CharField(max_length=-1, blank=True, null=True)
    sotano = models.FloatField(blank=True, null=True)
    estado_d_1 = models.CharField(max_length=-1, blank=True, null=True)
    agua_consu = models.CharField(max_length=-1, blank=True, null=True)
    desague = models.CharField(max_length=-1, blank=True, null=True)
    energia_el = models.CharField(max_length=-1, blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_catastro'


class GisCaracFcDensidadPoblacional(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    contourmin = models.FloatField(blank=True, null=True)
    contourmax = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_densidad_poblacional'


class GisCaracFcEstructuraVial(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    estado_via = models.CharField(max_length=-1, blank=True, null=True)
    conservaci = models.CharField(max_length=-1, blank=True, null=True)
    jerarquia = models.CharField(max_length=-1, blank=True, null=True)
    accesibili = models.CharField(max_length=-1, blank=True, null=True)
    habilitaci = models.CharField(max_length=-1, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    mostrar = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_estructura_vial'


class GisCaracFcEstructuraVialSecciones(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    corte = models.CharField(max_length=10, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_estructura_vial_secciones'


class GisCaracFcIluminacion(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_iluminacion'


class GisCaracFcInseguridad(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_inseguridad'


class GisCaracFcLineaFerrea(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    nomlinfer = models.CharField(max_length=254, blank=True, null=True)
    subnomlin = models.CharField(max_length=254, blank=True, null=True)
    tramo = models.CharField(max_length=254, blank=True, null=True)
    coddpto = models.CharField(max_length=254, blank=True, null=True)
    longkm = models.FloatField(blank=True, null=True)
    trocha = models.CharField(max_length=254, blank=True, null=True)
    electrif = models.CharField(max_length=254, blank=True, null=True)
    titular = models.CharField(max_length=254, blank=True, null=True)
    administ = models.CharField(max_length=254, blank=True, null=True)
    tipcont = models.BigIntegerField(blank=True, null=True)
    operador = models.CharField(max_length=254, blank=True, null=True)
    estfun = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_linea_ferrea'


class GisCaracFcLotes(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    ccodficha = models.CharField(max_length=25, blank=True, null=True)
    cregion = models.BigIntegerField(blank=True, null=True)
    cprovincia = models.BigIntegerField(blank=True, null=True)
    cdistrito = models.BigIntegerField(blank=True, null=True)
    ccodzre = models.CharField(max_length=10, blank=True, null=True)
    ccodapv = models.CharField(max_length=10, blank=True, null=True)
    cnombreapv = models.CharField(max_length=254, blank=True, null=True)
    ctipoagrup = models.CharField(max_length=254, blank=True, null=True)
    cmanzana = models.CharField(max_length=10, blank=True, null=True)
    clote = models.CharField(max_length=10, blank=True, null=True)
    csublote = models.CharField(max_length=10, blank=True, null=True)
    czre_ai = models.CharField(max_length=10, blank=True, null=True)
    csector = models.CharField(max_length=10, blank=True, null=True)
    ccondictit = models.CharField(max_length=25, blank=True, null=True)
    cnombtitu = models.CharField(max_length=75, blank=True, null=True)
    capaternot = models.CharField(max_length=25, blank=True, null=True)
    camaternot = models.CharField(max_length=25, blank=True, null=True)
    ctipodoc = models.CharField(max_length=10, blank=True, null=True)
    cnrodoc = models.CharField(max_length=10, blank=True, null=True)
    cnombconyu = models.CharField(max_length=25, blank=True, null=True)
    capaternoc = models.CharField(max_length=25, blank=True, null=True)
    camaternoc = models.CharField(max_length=25, blank=True, null=True)
    ctipopropi = models.CharField(max_length=20, blank=True, null=True)
    clugproced = models.CharField(max_length=75, blank=True, null=True)
    cformadqui = models.CharField(max_length=25, blank=True, null=True)
    dfechadqui = models.CharField(max_length=20, blank=True, null=True)
    cdocposlot = models.CharField(max_length=50, blank=True, null=True)
    crrrpp = models.CharField(max_length=10, blank=True, null=True)
    creshu = models.CharField(max_length=254, blank=True, null=True)
    dfechlichu = models.CharField(max_length=50, blank=True, null=True)
    csitactlot = models.CharField(max_length=50, blank=True, null=True)
    cusopredom = models.CharField(max_length=50, blank=True, null=True)
    cuso1erniv = models.CharField(max_length=50, blank=True, null=True)
    cusodetall = models.CharField(max_length=75, blank=True, null=True)
    cusosuelo = models.CharField(max_length=50, blank=True, null=True)
    iniv_bq_pr = models.BigIntegerField(blank=True, null=True)
    iunitsinmo = models.BigIntegerField(blank=True, null=True)
    isotanos = models.CharField(max_length=10, blank=True, null=True)
    ientretech = models.CharField(max_length=10, blank=True, null=True)
    cmateriapr = models.CharField(max_length=25, blank=True, null=True)
    cmodoconst = models.CharField(max_length=50, blank=True, null=True)
    cestadocon = models.CharField(max_length=10, blank=True, null=True)
    cconexagua = models.CharField(max_length=50, blank=True, null=True)
    caguadetal = models.CharField(max_length=50, blank=True, null=True)
    cdesague = models.CharField(max_length=50, blank=True, null=True)
    cconexee = models.CharField(max_length=50, blank=True, null=True)
    cservicelp = models.CharField(max_length=75, blank=True, null=True)
    fcoaguacom = models.CharField(max_length=15, blank=True, null=True)
    fcoaguasc = models.CharField(max_length=15, blank=True, null=True)
    fcoengelse = models.CharField(max_length=15, blank=True, null=True)
    fcotelef = models.CharField(max_length=15, blank=True, null=True)
    fcolimppub = models.CharField(max_length=15, blank=True, null=True)
    ifampropie = models.BigIntegerField(blank=True, null=True)
    ifaminqui = models.CharField(max_length=4, blank=True, null=True)
    imuje0_5 = models.BigIntegerField(blank=True, null=True)
    ivaro0_5 = models.BigIntegerField(blank=True, null=True)
    imuje6_12 = models.BigIntegerField(blank=True, null=True)
    ivaro6_12 = models.BigIntegerField(blank=True, null=True)
    imuje13_18 = models.BigIntegerField(blank=True, null=True)
    ivaro13_18 = models.BigIntegerField(blank=True, null=True)
    imuje19_30 = models.BigIntegerField(blank=True, null=True)
    ivaro19_30 = models.BigIntegerField(blank=True, null=True)
    imuje31_54 = models.BigIntegerField(blank=True, null=True)
    ivaro31_54 = models.BigIntegerField(blank=True, null=True)
    imuje55_65 = models.BigIntegerField(blank=True, null=True)
    ivaro55_65 = models.BigIntegerField(blank=True, null=True)
    imujem66 = models.BigIntegerField(blank=True, null=True)
    ivarom66 = models.BigIntegerField(blank=True, null=True)
    ifam = models.BigIntegerField(blank=True, null=True)
    ipoblactot = models.BigIntegerField(blank=True, null=True)
    inoleeesc = models.CharField(max_length=4, blank=True, null=True)
    isileeesc = models.CharField(max_length=10, blank=True, null=True)
    iprimaria = models.CharField(max_length=4, blank=True, null=True)
    isecundari = models.BigIntegerField(blank=True, null=True)
    itecnicsup = models.CharField(max_length=4, blank=True, null=True)
    isuperioru = models.CharField(max_length=4, blank=True, null=True)
    ctipo_he = models.CharField(max_length=20, blank=True, null=True)
    icant_phe = models.CharField(max_length=4, blank=True, null=True)
    cpartorgso = models.CharField(max_length=50, blank=True, null=True)
    cconocegrd = models.CharField(max_length=50, blank=True, null=True)
    isinseguro = models.BigIntegerField(blank=True, null=True)
    isis = models.BigIntegerField(blank=True, null=True)
    iffaa = models.CharField(max_length=10, blank=True, null=True)
    iessalud = models.BigIntegerField(blank=True, null=True)
    iprivado = models.CharField(max_length=4, blank=True, null=True)
    ctsersegur = models.CharField(max_length=25, blank=True, null=True)
    cactitudfr = models.CharField(max_length=254, blank=True, null=True)
    cingresofp = models.CharField(max_length=20, blank=True, null=True)
    cac_mercfi = models.CharField(max_length=25, blank=True, null=True)
    idesemplea = models.CharField(max_length=4, blank=True, null=True)
    idedicahog = models.BigIntegerField(blank=True, null=True)
    iocupadome = models.CharField(max_length=10, blank=True, null=True)
    iindependi = models.BigIntegerField(blank=True, null=True)
    idependien = models.BigIntegerField(blank=True, null=True)
    fcoautoval = models.CharField(max_length=20, blank=True, null=True)
    fcostcompv = models.CharField(max_length=75, blank=True, null=True)
    fcostventv = models.CharField(max_length=75, blank=True, null=True)
    fcoventalt = models.CharField(max_length=75, blank=True, null=True)
    calquiler = models.CharField(max_length=20, blank=True, null=True)
    fcostalqha = models.CharField(max_length=20, blank=True, null=True)
    fcostalqdp = models.CharField(max_length=20, blank=True, null=True)
    fcostalqvi = models.CharField(max_length=20, blank=True, null=True)
    cactecopri = models.CharField(max_length=75, blank=True, null=True)
    clugartrab = models.CharField(max_length=50, blank=True, null=True)
    icantpvale = models.BigIntegerField(blank=True, null=True)
    icantpjunt = models.CharField(max_length=10, blank=True, null=True)
    icantpqw = models.CharField(max_length=10, blank=True, null=True)
    icantpcunm = models.CharField(max_length=10, blank=True, null=True)
    icantppe65 = models.CharField(max_length=10, blank=True, null=True)
    icantpcont = models.CharField(max_length=10, blank=True, null=True)
    icantptrap = models.CharField(max_length=10, blank=True, null=True)
    icantpfise = models.CharField(max_length=10, blank=True, null=True)
    icantpsis = models.BigIntegerField(blank=True, null=True)
    icantpning = models.BigIntegerField(blank=True, null=True)
    cdisporrss = models.CharField(max_length=50, blank=True, null=True)
    ianimalesd = models.CharField(max_length=25, blank=True, null=True)
    ianimalesm = models.CharField(max_length=20, blank=True, null=True)
    cconsumo = models.CharField(max_length=20, blank=True, null=True)
    cventa = models.CharField(max_length=20, blank=True, null=True)
    ctpdispexc = models.CharField(max_length=75, blank=True, null=True)
    cconoceamb = models.CharField(max_length=75, blank=True, null=True)
    cmanejors = models.CharField(max_length=75, blank=True, null=True)
    cnecesidad = models.CharField(max_length=254, blank=True, null=True)
    ccasosinus = models.CharField(max_length=254, blank=True, null=True)
    cobservaci = models.CharField(max_length=254, blank=True, null=True)
    tenencia = models.CharField(max_length=50, blank=True, null=True)
    legalidad = models.CharField(max_length=50, blank=True, null=True)
    cusercrea = models.CharField(max_length=50, blank=True, null=True)
    cusermodi = models.CharField(max_length=50, blank=True, null=True)
    dfechacrea = models.CharField(max_length=25, blank=True, null=True)
    dfechamodi = models.CharField(max_length=25, blank=True, null=True)
    d0_5_años = models.FloatField(blank=True, null=True)
    d6_12_año = models.FloatField(blank=True, null=True)
    d12_15_añ = models.FloatField(blank=True, null=True)
    d16_30_añ = models.FloatField(blank=True, null=True)
    d31_50_añ = models.FloatField(blank=True, null=True)
    d51_60_añ = models.FloatField(blank=True, null=True)
    d61_64_añ = models.FloatField(blank=True, null=True)
    m_65_años = models.FloatField(blank=True, null=True)
    iniv_bq_1 = models.BigIntegerField(blank=True, null=True)
    iniv_bq_2 = models.FloatField(blank=True, null=True)
    iniv_bq_3 = models.FloatField(blank=True, null=True)
    iniv_bq_4 = models.FloatField(blank=True, null=True)
    id0_5 = models.FloatField(blank=True, null=True)
    id6_12 = models.FloatField(blank=True, null=True)
    id13_18 = models.FloatField(blank=True, null=True)
    id19_30 = models.FloatField(db_column='id19__30', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    id31_54 = models.FloatField(db_column='id31__54', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    id55_65 = models.FloatField(blank=True, null=True)
    im66 = models.FloatField(blank=True, null=True)
    fcoterrem2 = models.CharField(max_length=254, blank=True, null=True)
    cconsarver = models.CharField(max_length=254, blank=True, null=True)
    ccoptocont = models.CharField(max_length=254, blank=True, null=True)
    residenc_1 = models.CharField(max_length=254, blank=True, null=True)
    perdida_de = models.CharField(max_length=254, blank=True, null=True)
    conocimi_2 = models.CharField(max_length=254, blank=True, null=True)
    conoc_de_p = models.CharField(max_length=254, blank=True, null=True)
    cconflofau = models.CharField(max_length=254, blank=True, null=True)
    ocupacion_field = models.CharField(db_column='ocupacion_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    porcentaje = models.CharField(max_length=50, blank=True, null=True)
    clote_resi = models.CharField(max_length=254, blank=True, null=True)
    clote_ladr = models.CharField(max_length=254, blank=True, null=True)
    cning_otro = models.CharField(max_length=254, blank=True, null=True)
    cll_nomaso = models.CharField(max_length=254, blank=True, null=True)
    cll_nomemp = models.CharField(max_length=254, blank=True, null=True)
    cll_ruc = models.CharField(max_length=254, blank=True, null=True)
    cll_nompro = models.CharField(max_length=254, blank=True, null=True)
    cdplotros = models.CharField(max_length=254, blank=True, null=True)
    ccee_deta = models.CharField(max_length=254, blank=True, null=True)
    cslp_otros = models.CharField(max_length=254, blank=True, null=True)
    fcoaguacc = models.CharField(max_length=254, blank=True, null=True)
    inacvene = models.CharField(max_length=254, blank=True, null=True)
    inacperu = models.CharField(max_length=254, blank=True, null=True)
    ccuenta_ep = models.CharField(max_length=254, blank=True, null=True)
    fcostcomp = models.CharField(max_length=254, blank=True, null=True)
    canioactem = models.CharField(max_length=254, blank=True, null=True)
    ctipohorno = models.CharField(max_length=254, blank=True, null=True)
    cmate_comb = models.CharField(max_length=254, blank=True, null=True)
    cexcesopol = models.CharField(max_length=254, blank=True, null=True)
    cep_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    cep_afsalu = models.CharField(max_length=254, blank=True, null=True)
    cep_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexcesorui = models.CharField(max_length=254, blank=True, null=True)
    cer_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    cer_afsalu = models.CharField(max_length=254, blank=True, null=True)
    cer_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexcesohum = models.CharField(max_length=254, blank=True, null=True)
    ceh_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    ceh_afsalu = models.CharField(max_length=254, blank=True, null=True)
    ceh_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexvibr_ma = models.CharField(max_length=254, blank=True, null=True)
    cevm_tipma = models.CharField(max_length=254, blank=True, null=True)
    cdan_est_v = models.CharField(max_length=254, blank=True, null=True)
    cdev_parte = models.CharField(max_length=254, blank=True, null=True)
    cdevp_deta = models.CharField(max_length=254, blank=True, null=True)
    cveh_accvi = models.CharField(max_length=254, blank=True, null=True)
    cvavi_deta = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_lotes'


class GisCaracFcLotesHu(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.FloatField(blank=True, null=True)
    ambito = models.CharField(max_length=10, blank=True, null=True)
    admapkey_1 = models.FloatField(blank=True, null=True)
    textstring = models.CharField(max_length=254, blank=True, null=True)
    text_size = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    hu = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_lotes_hu'


class GisCaracFcLotesRevisarYurico(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    ccodficha = models.CharField(max_length=25, blank=True, null=True)
    cregion = models.BigIntegerField(blank=True, null=True)
    cprovincia = models.BigIntegerField(blank=True, null=True)
    cdistrito = models.BigIntegerField(blank=True, null=True)
    ccodzre = models.CharField(max_length=10, blank=True, null=True)
    ccodapv = models.CharField(max_length=10, blank=True, null=True)
    cnombreapv = models.CharField(max_length=254, blank=True, null=True)
    ctipoagrup = models.CharField(max_length=254, blank=True, null=True)
    cmanzana = models.CharField(max_length=10, blank=True, null=True)
    clote = models.CharField(max_length=10, blank=True, null=True)
    csublote = models.CharField(max_length=10, blank=True, null=True)
    czre_ai = models.CharField(max_length=10, blank=True, null=True)
    csector = models.CharField(max_length=10, blank=True, null=True)
    ccondictit = models.CharField(max_length=25, blank=True, null=True)
    cnombtitu = models.CharField(max_length=75, blank=True, null=True)
    capaternot = models.CharField(max_length=25, blank=True, null=True)
    camaternot = models.CharField(max_length=25, blank=True, null=True)
    ctipodoc = models.CharField(max_length=10, blank=True, null=True)
    cnrodoc = models.CharField(max_length=10, blank=True, null=True)
    cnombconyu = models.CharField(max_length=25, blank=True, null=True)
    capaternoc = models.CharField(max_length=25, blank=True, null=True)
    camaternoc = models.CharField(max_length=25, blank=True, null=True)
    ctipopropi = models.CharField(max_length=20, blank=True, null=True)
    clugproced = models.CharField(max_length=75, blank=True, null=True)
    cformadqui = models.CharField(max_length=25, blank=True, null=True)
    dfechadqui = models.CharField(max_length=20, blank=True, null=True)
    cdocposlot = models.CharField(max_length=50, blank=True, null=True)
    crrrpp = models.CharField(max_length=10, blank=True, null=True)
    creshu = models.CharField(max_length=254, blank=True, null=True)
    dfechlichu = models.CharField(max_length=50, blank=True, null=True)
    csitactlot = models.CharField(max_length=50, blank=True, null=True)
    cusopredom = models.CharField(max_length=50, blank=True, null=True)
    cuso1erniv = models.CharField(max_length=50, blank=True, null=True)
    cusodetall = models.CharField(max_length=75, blank=True, null=True)
    cusosuelo = models.CharField(max_length=50, blank=True, null=True)
    iniv_bq_pr = models.BigIntegerField(blank=True, null=True)
    iunitsinmo = models.BigIntegerField(blank=True, null=True)
    isotanos = models.CharField(max_length=10, blank=True, null=True)
    ientretech = models.CharField(max_length=10, blank=True, null=True)
    cmateriapr = models.CharField(max_length=25, blank=True, null=True)
    cmodoconst = models.CharField(max_length=50, blank=True, null=True)
    cestadocon = models.CharField(max_length=10, blank=True, null=True)
    cconexagua = models.CharField(max_length=50, blank=True, null=True)
    caguadetal = models.CharField(max_length=50, blank=True, null=True)
    cdesague = models.CharField(max_length=50, blank=True, null=True)
    cconexee = models.CharField(max_length=50, blank=True, null=True)
    cservicelp = models.CharField(max_length=75, blank=True, null=True)
    fcoaguacom = models.CharField(max_length=15, blank=True, null=True)
    fcoaguasc = models.CharField(max_length=15, blank=True, null=True)
    fcoengelse = models.CharField(max_length=15, blank=True, null=True)
    fcotelef = models.CharField(max_length=15, blank=True, null=True)
    fcolimppub = models.CharField(max_length=15, blank=True, null=True)
    ifampropie = models.BigIntegerField(blank=True, null=True)
    ifaminqui = models.CharField(max_length=4, blank=True, null=True)
    imuje0_5 = models.BigIntegerField(blank=True, null=True)
    ivaro0_5 = models.BigIntegerField(blank=True, null=True)
    imuje6_12 = models.BigIntegerField(blank=True, null=True)
    ivaro6_12 = models.BigIntegerField(blank=True, null=True)
    imuje13_18 = models.BigIntegerField(blank=True, null=True)
    ivaro13_18 = models.BigIntegerField(blank=True, null=True)
    imuje19_30 = models.BigIntegerField(blank=True, null=True)
    ivaro19_30 = models.BigIntegerField(blank=True, null=True)
    imuje31_54 = models.BigIntegerField(blank=True, null=True)
    ivaro31_54 = models.BigIntegerField(blank=True, null=True)
    imuje55_65 = models.BigIntegerField(blank=True, null=True)
    ivaro55_65 = models.BigIntegerField(blank=True, null=True)
    imujem66 = models.BigIntegerField(blank=True, null=True)
    ivarom66 = models.BigIntegerField(blank=True, null=True)
    ifam = models.BigIntegerField(blank=True, null=True)
    ipoblactot = models.BigIntegerField(blank=True, null=True)
    inoleeesc = models.CharField(max_length=4, blank=True, null=True)
    isileeesc = models.CharField(max_length=10, blank=True, null=True)
    iprimaria = models.CharField(max_length=4, blank=True, null=True)
    isecundari = models.BigIntegerField(blank=True, null=True)
    itecnicsup = models.CharField(max_length=4, blank=True, null=True)
    isuperioru = models.CharField(max_length=4, blank=True, null=True)
    ctipo_he = models.CharField(max_length=20, blank=True, null=True)
    icant_phe = models.CharField(max_length=4, blank=True, null=True)
    cpartorgso = models.CharField(max_length=50, blank=True, null=True)
    cconocegrd = models.CharField(max_length=50, blank=True, null=True)
    isinseguro = models.BigIntegerField(blank=True, null=True)
    isis = models.BigIntegerField(blank=True, null=True)
    iffaa = models.CharField(max_length=10, blank=True, null=True)
    iessalud = models.BigIntegerField(blank=True, null=True)
    iprivado = models.CharField(max_length=4, blank=True, null=True)
    ctsersegur = models.CharField(max_length=25, blank=True, null=True)
    cactitudfr = models.CharField(max_length=254, blank=True, null=True)
    cingresofp = models.CharField(max_length=20, blank=True, null=True)
    cac_mercfi = models.CharField(max_length=25, blank=True, null=True)
    idesemplea = models.CharField(max_length=4, blank=True, null=True)
    idedicahog = models.BigIntegerField(blank=True, null=True)
    iocupadome = models.CharField(max_length=10, blank=True, null=True)
    iindependi = models.BigIntegerField(blank=True, null=True)
    idependien = models.BigIntegerField(blank=True, null=True)
    fcoautoval = models.CharField(max_length=20, blank=True, null=True)
    fcostcompv = models.CharField(max_length=75, blank=True, null=True)
    fcostventv = models.CharField(max_length=75, blank=True, null=True)
    fcoventalt = models.CharField(max_length=75, blank=True, null=True)
    calquiler = models.CharField(max_length=20, blank=True, null=True)
    fcostalqha = models.CharField(max_length=20, blank=True, null=True)
    fcostalqdp = models.CharField(max_length=20, blank=True, null=True)
    fcostalqvi = models.CharField(max_length=20, blank=True, null=True)
    cactecopri = models.CharField(max_length=75, blank=True, null=True)
    clugartrab = models.CharField(max_length=50, blank=True, null=True)
    icantpvale = models.BigIntegerField(blank=True, null=True)
    icantpjunt = models.CharField(max_length=10, blank=True, null=True)
    icantpqw = models.CharField(max_length=10, blank=True, null=True)
    icantpcunm = models.CharField(max_length=10, blank=True, null=True)
    icantppe65 = models.CharField(max_length=10, blank=True, null=True)
    icantpcont = models.CharField(max_length=10, blank=True, null=True)
    icantptrap = models.CharField(max_length=10, blank=True, null=True)
    icantpfise = models.CharField(max_length=10, blank=True, null=True)
    icantpsis = models.BigIntegerField(blank=True, null=True)
    icantpning = models.BigIntegerField(blank=True, null=True)
    cdisporrss = models.CharField(max_length=50, blank=True, null=True)
    ianimalesd = models.CharField(max_length=25, blank=True, null=True)
    ianimalesm = models.CharField(max_length=20, blank=True, null=True)
    cconsumo = models.CharField(max_length=20, blank=True, null=True)
    cventa = models.CharField(max_length=20, blank=True, null=True)
    ctpdispexc = models.CharField(max_length=75, blank=True, null=True)
    cconoceamb = models.CharField(max_length=75, blank=True, null=True)
    cmanejors = models.CharField(max_length=75, blank=True, null=True)
    cnecesidad = models.CharField(max_length=254, blank=True, null=True)
    ccasosinus = models.CharField(max_length=254, blank=True, null=True)
    cobservaci = models.CharField(max_length=254, blank=True, null=True)
    tenencia = models.CharField(max_length=50, blank=True, null=True)
    legalidad = models.CharField(max_length=50, blank=True, null=True)
    cusercrea = models.CharField(max_length=50, blank=True, null=True)
    cusermodi = models.CharField(max_length=50, blank=True, null=True)
    dfechacrea = models.CharField(max_length=25, blank=True, null=True)
    dfechamodi = models.CharField(max_length=25, blank=True, null=True)
    d0_5_años = models.FloatField(blank=True, null=True)
    d6_12_año = models.FloatField(blank=True, null=True)
    d12_15_añ = models.FloatField(blank=True, null=True)
    d16_30_añ = models.FloatField(blank=True, null=True)
    d31_50_añ = models.FloatField(blank=True, null=True)
    d51_60_añ = models.FloatField(blank=True, null=True)
    d61_64_añ = models.FloatField(blank=True, null=True)
    m_65_años = models.FloatField(blank=True, null=True)
    iniv_bq_1 = models.BigIntegerField(blank=True, null=True)
    iniv_bq_2 = models.FloatField(blank=True, null=True)
    iniv_bq_3 = models.FloatField(blank=True, null=True)
    iniv_bq_4 = models.FloatField(blank=True, null=True)
    id0_5 = models.FloatField(blank=True, null=True)
    id6_12 = models.FloatField(blank=True, null=True)
    id13_18 = models.FloatField(blank=True, null=True)
    id19_30 = models.FloatField(db_column='id19__30', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    id31_54 = models.FloatField(db_column='id31__54', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    id55_65 = models.FloatField(blank=True, null=True)
    im66 = models.FloatField(blank=True, null=True)
    fcoterrem2 = models.CharField(max_length=254, blank=True, null=True)
    cconsarver = models.CharField(max_length=254, blank=True, null=True)
    ccoptocont = models.CharField(max_length=254, blank=True, null=True)
    perdida_de = models.CharField(max_length=254, blank=True, null=True)
    conocimi_2 = models.CharField(max_length=254, blank=True, null=True)
    conoc_de_p = models.CharField(max_length=254, blank=True, null=True)
    cconflofau = models.CharField(max_length=254, blank=True, null=True)
    clote_resi = models.CharField(max_length=254, blank=True, null=True)
    clote_ladr = models.CharField(max_length=254, blank=True, null=True)
    cning_otro = models.CharField(max_length=254, blank=True, null=True)
    cll_nomaso = models.CharField(max_length=254, blank=True, null=True)
    cll_nomemp = models.CharField(max_length=254, blank=True, null=True)
    cll_ruc = models.CharField(max_length=254, blank=True, null=True)
    cll_nompro = models.CharField(max_length=254, blank=True, null=True)
    cdplotros = models.CharField(max_length=254, blank=True, null=True)
    ccee_deta = models.CharField(max_length=254, blank=True, null=True)
    cslp_otros = models.CharField(max_length=254, blank=True, null=True)
    fcoaguacc = models.CharField(max_length=254, blank=True, null=True)
    inacvene = models.CharField(max_length=254, blank=True, null=True)
    inacperu = models.CharField(max_length=254, blank=True, null=True)
    ccuenta_ep = models.CharField(max_length=254, blank=True, null=True)
    fcostcomp = models.CharField(max_length=254, blank=True, null=True)
    canioactem = models.CharField(max_length=254, blank=True, null=True)
    ctipohorno = models.CharField(max_length=254, blank=True, null=True)
    cmate_comb = models.CharField(max_length=254, blank=True, null=True)
    cexcesopol = models.CharField(max_length=254, blank=True, null=True)
    cep_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    cep_afsalu = models.CharField(max_length=254, blank=True, null=True)
    cep_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexcesorui = models.CharField(max_length=254, blank=True, null=True)
    cer_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    cer_afsalu = models.CharField(max_length=254, blank=True, null=True)
    cer_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexcesohum = models.CharField(max_length=254, blank=True, null=True)
    ceh_hh_dd = models.CharField(max_length=254, blank=True, null=True)
    ceh_afsalu = models.CharField(max_length=254, blank=True, null=True)
    ceh_afscom = models.CharField(max_length=254, blank=True, null=True)
    cexvibr_ma = models.CharField(max_length=254, blank=True, null=True)
    cevm_tipma = models.CharField(max_length=254, blank=True, null=True)
    cdan_est_v = models.CharField(max_length=254, blank=True, null=True)
    cdev_parte = models.CharField(max_length=254, blank=True, null=True)
    cdevp_deta = models.CharField(max_length=254, blank=True, null=True)
    cveh_accvi = models.CharField(max_length=254, blank=True, null=True)
    cvavi_deta = models.CharField(max_length=254, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    cmanzana_p = models.CharField(max_length=5, blank=True, null=True)
    clote_plan = models.CharField(max_length=5, blank=True, null=True)
    csublote_p = models.CharField(max_length=5, blank=True, null=True)
    crianza_an = models.CharField(max_length=50, blank=True, null=True)
    isolo_lee = models.CharField(max_length=10, blank=True, null=True)
    tipo_resid = models.CharField(max_length=50, blank=True, null=True)
    porc_pers_field = models.CharField(db_column='porc_pers_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    clote_x = models.CharField(max_length=5, blank=True, null=True)
    clote_y = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_lotes_revisar_yurico'


class GisCaracFcManzanas(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    manzana = models.CharField(max_length=254, blank=True, null=True)
    poblacion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    agrupacion = models.CharField(max_length=100, blank=True, null=True)
    area_libre = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    frente_min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    densidad_n = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_manzanas'


class GisCaracFcManzanasAmbito(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    codigo_manzana = models.CharField(max_length=254, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_manzanas_ambito'


class GisCaracFcManzanasContexto(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.BigIntegerField(blank=True, null=True)
    zonificaci = models.CharField(max_length=30, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    ubicacion = models.CharField(max_length=30, blank=True, null=True)
    manzana = models.FloatField(blank=True, null=True)
    comunidad = models.CharField(max_length=50, blank=True, null=True)
    zoni_criti = models.CharField(max_length=50, blank=True, null=True)
    zoni_z = models.CharField(max_length=20, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_manzanas_contexto'


class GisCaracFcManzanasHu(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    admapkey = models.FloatField(blank=True, null=True)
    ambito = models.CharField(max_length=-1, blank=True, null=True)
    admapkey_1 = models.FloatField(blank=True, null=True)
    textstring = models.CharField(max_length=-1, blank=True, null=True)
    text_size = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    hu = models.CharField(max_length=-1, blank=True, null=True)
    uso = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_manzanas_hu'


class GisCaracFcParaderos(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    paradero = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(srid=32719, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    ruta = models.CharField(max_length=10, blank=True, null=True)
    cod_ruta = models.SmallIntegerField(blank=True, null=True)
    nom_et = models.CharField(max_length=200, blank=True, null=True)
    nom_parade = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_paraderos'


class GisCaracFcPostesAlumbradoPublico(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    fid_zona_i = models.BigIntegerField(blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    fid_fcequi = models.BigIntegerField(blank=True, null=True)
    objectid_1 = models.BigIntegerField(blank=True, null=True)
    codigoempr = models.CharField(max_length=3, blank=True, null=True)
    codigosucu = models.CharField(max_length=3, blank=True, null=True)
    codigotecn = models.CharField(max_length=7, blank=True, null=True)
    codigote_1 = models.CharField(max_length=2, blank=True, null=True)
    codigonodo = models.CharField(max_length=15, blank=True, null=True)
    codigoequi = models.CharField(max_length=15, blank=True, null=True)
    codigotipo = models.CharField(max_length=15, blank=True, null=True)
    codigoti_1 = models.CharField(max_length=15, blank=True, null=True)
    codigoti_2 = models.CharField(max_length=15, blank=True, null=True)
    cantidadla = models.BigIntegerField(blank=True, null=True)
    codigoesta = models.CharField(max_length=3, blank=True, null=True)
    codpropiet = models.CharField(max_length=15, blank=True, null=True)
    codigoes_1 = models.CharField(max_length=3, blank=True, null=True)
    usuariocre = models.CharField(max_length=20, blank=True, null=True)
    usuariomod = models.CharField(max_length=20, blank=True, null=True)
    fechacreac = models.DateField(blank=True, null=True)
    fechamodif = models.DateField(blank=True, null=True)
    angulo = models.FloatField(blank=True, null=True)
    longitudhp = models.FloatField(blank=True, null=True)
    longitudvp = models.FloatField(blank=True, null=True)
    anguloincl = models.FloatField(blank=True, null=True)
    fechainsta = models.DateField(blank=True, null=True)
    ultimafech = models.DateField(blank=True, null=True)
    codigoobra = models.CharField(max_length=15, blank=True, null=True)
    codigomarc = models.CharField(max_length=15, blank=True, null=True)
    codigomode = models.CharField(max_length=15, blank=True, null=True)
    fechains_1 = models.DateField(blank=True, null=True)
    luminarias = models.CharField(max_length=1, blank=True, null=True)
    ultimafe_1 = models.DateField(blank=True, null=True)
    codigoob_1 = models.CharField(max_length=15, blank=True, null=True)
    codigoma_1 = models.CharField(max_length=15, blank=True, null=True)
    fechains_2 = models.DateField(blank=True, null=True)
    ultimafe_2 = models.DateField(blank=True, null=True)
    codigoob_2 = models.CharField(max_length=15, blank=True, null=True)
    formalampa = models.CharField(max_length=1, blank=True, null=True)
    codigoma_2 = models.CharField(max_length=15, blank=True, null=True)
    codigomo_1 = models.CharField(max_length=15, blank=True, null=True)
    potenciaba = models.FloatField(blank=True, null=True)
    fechains_3 = models.DateField(blank=True, null=True)
    ultimafe_3 = models.DateField(blank=True, null=True)
    codigoma_3 = models.CharField(max_length=15, blank=True, null=True)
    codigomo_2 = models.CharField(max_length=15, blank=True, null=True)
    fechains_4 = models.DateField(blank=True, null=True)
    ultimafe_4 = models.DateField(blank=True, null=True)
    codigotram = models.CharField(max_length=15, blank=True, null=True)
    codigoubic = models.CharField(max_length=2, blank=True, null=True)
    codigotr_1 = models.CharField(max_length=15, blank=True, null=True)
    codigoparq = models.CharField(max_length=15, blank=True, null=True)
    potenciala = models.FloatField(blank=True, null=True)
    codigoob_3 = models.CharField(max_length=15, blank=True, null=True)
    vnr = models.CharField(max_length=2, blank=True, null=True)
    codigomate = models.CharField(max_length=6, blank=True, null=True)
    codigoti_3 = models.CharField(max_length=3, blank=True, null=True)
    codigoti_4 = models.CharField(max_length=3, blank=True, null=True)
    deficienci = models.CharField(max_length=20, blank=True, null=True)
    conector = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_postes_alumbrado_publico'


class GisCaracFcQuebradas(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    fid_field = models.IntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    entity = models.CharField(max_length=-1, blank=True, null=True)
    layer = models.CharField(max_length=-1, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    linetype = models.CharField(max_length=-1, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    linewt = models.IntegerField(blank=True, null=True)
    refname = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_quebradas'


class GisCaracFcQuebradasPolygon(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    predios = models.CharField(max_length=-1, blank=True, null=True)
    predio = models.CharField(max_length=-1, blank=True, null=True)
    tipologia = models.CharField(max_length=-1, blank=True, null=True)
    sotano = models.FloatField(blank=True, null=True)
    material_d = models.CharField(max_length=-1, blank=True, null=True)
    estado_de = models.CharField(max_length=-1, blank=True, null=True)
    estado_d_1 = models.CharField(max_length=-1, blank=True, null=True)
    agua_consu = models.CharField(max_length=-1, blank=True, null=True)
    desague = models.CharField(max_length=-1, blank=True, null=True)
    energia_el = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_quebradas_polygon'


class GisCaracFcRedAguaPotable(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    codidred = models.CharField(max_length=-1, blank=True, null=True)
    d_tipo = models.CharField(max_length=-1, blank=True, null=True)
    d_xdiametr = models.CharField(max_length=-1, blank=True, null=True)
    d_xmateria = models.CharField(max_length=-1, blank=True, null=True)
    d_yantigue = models.CharField(max_length=-1, blank=True, null=True)
    d_yfechaca = models.CharField(max_length=-1, blank=True, null=True)
    d_yprofund = models.CharField(max_length=-1, blank=True, null=True)
    d_yreferen = models.CharField(max_length=-1, blank=True, null=True)
    longitudre = models.FloatField(blank=True, null=True)
    situacion = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_red_agua_potable'


class GisCaracFcRedDesague(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    featid1 = models.FloatField(blank=True, null=True)
    antiguedad = models.CharField(max_length=-1, blank=True, null=True)
    calle = models.CharField(max_length=-1, blank=True, null=True)
    diametro = models.CharField(max_length=-1, blank=True, null=True)
    idmicrosec = models.CharField(max_length=-1, blank=True, null=True)
    idzona = models.CharField(max_length=-1, blank=True, null=True)
    material = models.CharField(max_length=-1, blank=True, null=True)
    observacio = models.CharField(max_length=-1, blank=True, null=True)
    profundida = models.CharField(max_length=-1, blank=True, null=True)
    referencia = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    situacion = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_red_desague'


class GisCaracFcRedElectFranjaAltaTension(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.FloatField(blank=True, null=True)
    linea_tran = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=20, blank=True, null=True)
    longitud = models.CharField(max_length=20, blank=True, null=True)
    tension = models.CharField(max_length=20, blank=True, null=True)
    material_s = models.CharField(max_length=50, blank=True, null=True)
    tipo_sopor = models.CharField(max_length=50, blank=True, null=True)
    material_c = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_red_elect_franja_alta_tension'


class GisCaracFcRedElectFranjaMedianaTension(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_red_elect_franja_mediana_tension'


class GisCaracFcReservorios(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    cod_inf = models.CharField(max_length=-1, blank=True, null=True)
    grupo = models.CharField(max_length=-1, blank=True, null=True)
    long_km = models.FloatField(blank=True, null=True)
    nombdist = models.CharField(max_length=-1, blank=True, null=True)
    nombprov = models.CharField(max_length=-1, blank=True, null=True)
    nombdep = models.CharField(max_length=-1, blank=True, null=True)
    observ = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    nom_eq = models.CharField(max_length=-1, blank=True, null=True)
    volumen = models.FloatField(blank=True, null=True)
    antigüeda = models.FloatField(db_column='antigÜeda', blank=True, null=True)  # Field name made lowercase.
    estado_fis = models.CharField(max_length=-1, blank=True, null=True)
    operativo = models.CharField(max_length=-1, blank=True, null=True)
    continuida = models.FloatField(blank=True, null=True)
    conexiones = models.FloatField(blank=True, null=True)
    cont_prom = models.FloatField(blank=True, null=True)
    sistema = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_reservorios'


class GisCaracFcRobos(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_robos'


class GisCaracFcRutasTransportePublico(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    estado_via = models.CharField(max_length=-1, blank=True, null=True)
    conservaci = models.CharField(max_length=-1, blank=True, null=True)
    jerarquia = models.CharField(max_length=-1, blank=True, null=True)
    accesibili = models.CharField(max_length=-1, blank=True, null=True)
    habilitaci = models.CharField(max_length=-1, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_rutas_transporte_publico'


class GisCaracFcRutasTransportePublicoFull(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    ruta = models.CharField(max_length=5, blank=True, null=True)
    cod_ru = models.FloatField(blank=True, null=True)
    nom_et = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=7, blank=True, null=True)
    nom_direcc = models.CharField(max_length=100, blank=True, null=True)
    nom_dist = models.CharField(max_length=15, blank=True, null=True)
    flota_requ = models.FloatField(blank=True, null=True)
    flota_reqm = models.FloatField(blank=True, null=True)
    recor_inic = models.FloatField(blank=True, null=True)
    recor_km = models.FloatField(blank=True, null=True)
    n_pasajero = models.FloatField(blank=True, null=True)
    n_vueltas = models.FloatField(blank=True, null=True)
    fuente = models.CharField(max_length=150, blank=True, null=True)
    horario = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_rutas_transporte_publico_full'


class GisCaracFcSaneamientoBasico(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    predios = models.CharField(max_length=-1, blank=True, null=True)
    predio = models.CharField(max_length=-1, blank=True, null=True)
    tipologia = models.CharField(max_length=-1, blank=True, null=True)
    nivel_de_e = models.FloatField(blank=True, null=True)
    sotano = models.FloatField(blank=True, null=True)
    material_d = models.CharField(max_length=-1, blank=True, null=True)
    estado_de = models.CharField(max_length=-1, blank=True, null=True)
    estado_d_1 = models.CharField(max_length=-1, blank=True, null=True)
    agua_consu = models.CharField(max_length=-1, blank=True, null=True)
    desague = models.CharField(max_length=-1, blank=True, null=True)
    energia_el = models.CharField(max_length=-1, blank=True, null=True)
    objectid_1 = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=-1, blank=True, null=True)
    predios_1 = models.CharField(max_length=-1, blank=True, null=True)
    uso = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_saneamiento_basico'


class GisCaracFcSeccionesVias(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    corte = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_secciones_vias'


class GisCaracFcSituacionLegalPredios(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    legal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_situacion_legal_predios'


class GisCaracFcViasPendientes(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    text = models.CharField(max_length=-1, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    estado_via = models.CharField(max_length=-1, blank=True, null=True)
    conservaci = models.CharField(max_length=-1, blank=True, null=True)
    jerarquia = models.CharField(max_length=-1, blank=True, null=True)
    accesibili = models.CharField(max_length=-1, blank=True, null=True)
    habilitaci = models.CharField(max_length=-1, blank=True, null=True)
    segmento = models.CharField(max_length=-1, blank=True, null=True)
    pendiente1 = models.CharField(max_length=-1, blank=True, null=True)
    pendiente2 = models.CharField(max_length=-1, blank=True, null=True)
    mostrar = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fc_vias_pendientes'


class GisCaracFlAportesHu(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    uso = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    hu = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    ambito = models.CharField(max_length=100, blank=True, null=True)
    manzana = models.CharField(max_length=20, blank=True, null=True)
    lote = models.CharField(max_length=20, blank=True, null=True)
    resolucion_hu = models.CharField(max_length=200, blank=True, null=True)
    codigo_uso = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_fl_aportes_hu'


class GisCaracGrdOcupacionZonasPeligro(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_grd_ocupacion_zonas_peligro'


class GisCaracGrdPeligros(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    valor_peli = models.FloatField(blank=True, null=True)
    nivel_peli = models.CharField(max_length=15, blank=True, null=True)
    rango_peli = models.CharField(max_length=50, blank=True, null=True)
    tipo_pelig = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    area_m2 = models.FloatField(blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    observacio = models.CharField(max_length=30, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_grd_peligros'


class GisCaracGrdRiesgos(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    tipo_pelig = models.CharField(max_length=50, blank=True, null=True)
    valor_peli = models.FloatField(blank=True, null=True)
    nivel_peli = models.CharField(max_length=15, blank=True, null=True)
    valor_vuln = models.FloatField(blank=True, null=True)
    nivel_vuln = models.CharField(max_length=15, blank=True, null=True)
    valor_ries = models.FloatField(blank=True, null=True)
    nivel_ries = models.CharField(max_length=15, blank=True, null=True)
    cond_predi = models.CharField(max_length=50, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_grd_riesgos'


class GisCaracGrdVulnerabilidad(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    tipologia = models.CharField(max_length=15, blank=True, null=True)
    hab_lote = models.FloatField(blank=True, null=True)
    acceso_ssb = models.FloatField(blank=True, null=True)
    grupo_etar = models.FloatField(blank=True, null=True)
    conoci_grd = models.FloatField(blank=True, null=True)
    org_social = models.FloatField(blank=True, null=True)
    locali_pel = models.FloatField(blank=True, null=True)
    material_c = models.FloatField(blank=True, null=True)
    estado_con = models.FloatField(blank=True, null=True)
    ocupacion = models.FloatField(blank=True, null=True)
    pea = models.FloatField(blank=True, null=True)
    ingreso_fa = models.FloatField(blank=True, null=True)
    cerca_rrss = models.FloatField(blank=True, null=True)
    disp_excre = models.FloatField(blank=True, null=True)
    disp_rrss = models.FloatField(blank=True, null=True)
    manej_rrss = models.FloatField(blank=True, null=True)
    conoci_amb = models.FloatField(blank=True, null=True)
    vuln_socia = models.FloatField(blank=True, null=True)
    vuln_econo = models.FloatField(blank=True, null=True)
    vuln_ambie = models.FloatField(blank=True, null=True)
    valor_vuln = models.FloatField(blank=True, null=True)
    nivel_vuln = models.CharField(max_length=50, blank=True, null=True)
    rango_vuln = models.CharField(max_length=25, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_carac_grd_vulnerabilidad'


class GisCaractEvarPeligroCaidaSuelos(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    rango_pendiente = models.CharField(max_length=20, blank=True, null=True)
    descrip_pendiente = models.CharField(max_length=50, blank=True, null=True)
    ponderacion_pendiente = models.FloatField(blank=True, null=True)
    d_p1 = models.FloatField(blank=True, null=True)
    p_1 = models.FloatField(blank=True, null=True)
    simb_geologico = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    unid_geologica = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.CharField(max_length=254, blank=True, null=True)
    pond_geologica = models.FloatField(blank=True, null=True)
    d_p3 = models.FloatField(blank=True, null=True)
    p_3 = models.FloatField(blank=True, null=True)
    rang_areas = models.CharField(max_length=150, blank=True, null=True)
    d_p_area = models.FloatField(blank=True, null=True)
    d_pe = models.FloatField(blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    altura_r = models.CharField(max_length=10, blank=True, null=True)
    d_altura = models.FloatField(blank=True, null=True)
    d_p2 = models.FloatField(blank=True, null=True)
    p_2 = models.FloatField(blank=True, null=True)
    v_peli = models.FloatField(blank=True, null=True)
    susc = models.FloatField(blank=True, null=True)
    nivel_peligro = models.CharField(max_length=10, blank=True, null=True)
    v_peli2 = models.FloatField(blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_caract_evar_peligro_caida_suelos'


class GisCaractEvarRiesgo(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    ccodfich_1 = models.CharField(max_length=254, blank=True, null=True)
    fid_1 = models.BigIntegerField(blank=True, null=True)
    ccodficha = models.CharField(max_length=50, blank=True, null=True)
    new_distan = models.CharField(max_length=50, blank=True, null=True)
    ccodfich_2 = models.CharField(max_length=254, blank=True, null=True)
    csitactlot = models.CharField(max_length=254, blank=True, null=True)
    cusosuelo = models.CharField(max_length=254, blank=True, null=True)
    cusopredom = models.CharField(max_length=254, blank=True, null=True)
    n_p_lote = models.BigIntegerField(blank=True, null=True)
    d_n_p_lote = models.FloatField(blank=True, null=True)
    p_n_p = models.FloatField(blank=True, null=True)
    ge_05_m66 = models.BigIntegerField(blank=True, null=True)
    ge_6_12_55 = models.BigIntegerField(blank=True, null=True)
    ge_13_18 = models.BigIntegerField(blank=True, null=True)
    ge_19_30 = models.BigIntegerField(blank=True, null=True)
    ge_31_54 = models.BigIntegerField(blank=True, null=True)
    poblacion_field = models.BigIntegerField(db_column='poblacion_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ge_pred = models.CharField(max_length=254, blank=True, null=True)
    d_ge = models.FloatField(blank=True, null=True)
    p_ge = models.FloatField(blank=True, null=True)
    ssbb = models.CharField(max_length=254, blank=True, null=True)
    d_ssbb = models.FloatField(blank=True, null=True)
    d_ssbb2 = models.FloatField(blank=True, null=True)
    grd = models.CharField(max_length=254, blank=True, null=True)
    d_grd = models.FloatField(blank=True, null=True)
    p_grd = models.FloatField(blank=True, null=True)
    org_pob = models.CharField(max_length=254, blank=True, null=True)
    d_org_pob = models.FloatField(blank=True, null=True)
    p_org_pob = models.FloatField(blank=True, null=True)
    v_social = models.FloatField(blank=True, null=True)
    l_edifi = models.CharField(max_length=254, blank=True, null=True)
    d_l_edif = models.FloatField(blank=True, null=True)
    p_l_edif = models.FloatField(blank=True, null=True)
    mater = models.CharField(max_length=254, blank=True, null=True)
    d_mater = models.FloatField(blank=True, null=True)
    p_mater = models.FloatField(blank=True, null=True)
    conser = models.CharField(max_length=254, blank=True, null=True)
    d_conser = models.FloatField(blank=True, null=True)
    p_conser = models.FloatField(blank=True, null=True)
    ocupa_pred = models.CharField(max_length=254, blank=True, null=True)
    d_ocu = models.FloatField(blank=True, null=True)
    p_ocu = models.FloatField(blank=True, null=True)
    v_economic = models.FloatField(blank=True, null=True)
    c_horno = models.CharField(max_length=254, blank=True, null=True)
    d_c_horno = models.FloatField(blank=True, null=True)
    p_c_horno = models.FloatField(blank=True, null=True)
    disp_rrss_field = models.CharField(db_column='disp_rrss_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    d_disp_rrs = models.FloatField(blank=True, null=True)
    p_dis_rrss = models.FloatField(blank=True, null=True)
    disp_excre = models.CharField(max_length=254, blank=True, null=True)
    d_disp_exc = models.FloatField(blank=True, null=True)
    p_disp_exc = models.FloatField(blank=True, null=True)
    m_rrss_ind = models.CharField(max_length=254, blank=True, null=True)
    d_m_rrss_i = models.FloatField(blank=True, null=True)
    p_m_rrss = models.FloatField(blank=True, null=True)
    c_amb = models.CharField(max_length=254, blank=True, null=True)
    d_c_amb = models.FloatField(blank=True, null=True)
    p_c_amb = models.FloatField(blank=True, null=True)
    v_ambienta = models.FloatField(blank=True, null=True)
    v_v = models.FloatField(blank=True, null=True)
    niv_vulne = models.CharField(max_length=15, blank=True, null=True)
    nivel_peligro = models.CharField(max_length=10, blank=True, null=True)
    nivel_riesgo = models.CharField(max_length=15, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_caract_evar_riesgo'


class GisCaractEvarUnidadesGeologicas(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    unidades_geologicas = models.CharField(max_length=20, blank=True, null=True)
    simbolos_geologicos = models.CharField(max_length=20, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_caract_evar_unidades_geologicas'


class GisCaractEvarVulnerabilidad(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    ccodfich_1 = models.CharField(max_length=254, blank=True, null=True)
    fid_1 = models.BigIntegerField(blank=True, null=True)
    ccodficha = models.CharField(max_length=50, blank=True, null=True)
    new_distan = models.CharField(max_length=50, blank=True, null=True)
    ccodfich_2 = models.CharField(max_length=254, blank=True, null=True)
    csitactlot = models.CharField(max_length=254, blank=True, null=True)
    cusosuelo = models.CharField(max_length=254, blank=True, null=True)
    cusopredom = models.CharField(max_length=254, blank=True, null=True)
    n_p_lote = models.BigIntegerField(blank=True, null=True)
    d_n_p_lote = models.FloatField(blank=True, null=True)
    p_n_p = models.FloatField(blank=True, null=True)
    ge_05_m66 = models.BigIntegerField(blank=True, null=True)
    ge_6_12_55 = models.BigIntegerField(blank=True, null=True)
    ge_13_18 = models.BigIntegerField(blank=True, null=True)
    ge_19_30 = models.BigIntegerField(blank=True, null=True)
    ge_31_54 = models.BigIntegerField(blank=True, null=True)
    poblacion_field = models.BigIntegerField(db_column='poblacion_', blank=True, null=True)  # Field renamed because it ended with '_'.
    ge_pred = models.CharField(max_length=254, blank=True, null=True)
    d_ge = models.FloatField(blank=True, null=True)
    p_ge = models.FloatField(blank=True, null=True)
    ssbb = models.CharField(max_length=254, blank=True, null=True)
    d_ssbb = models.FloatField(blank=True, null=True)
    d_ssbb2 = models.FloatField(blank=True, null=True)
    grd = models.CharField(max_length=254, blank=True, null=True)
    d_grd = models.FloatField(blank=True, null=True)
    p_grd = models.FloatField(blank=True, null=True)
    org_pob = models.CharField(max_length=254, blank=True, null=True)
    d_org_pob = models.FloatField(blank=True, null=True)
    p_org_pob = models.FloatField(blank=True, null=True)
    v_social = models.FloatField(blank=True, null=True)
    l_edifi = models.CharField(max_length=254, blank=True, null=True)
    d_l_edif = models.FloatField(blank=True, null=True)
    p_l_edif = models.FloatField(blank=True, null=True)
    mater = models.CharField(max_length=254, blank=True, null=True)
    d_mater = models.FloatField(blank=True, null=True)
    p_mater = models.FloatField(blank=True, null=True)
    conser = models.CharField(max_length=254, blank=True, null=True)
    d_conser = models.FloatField(blank=True, null=True)
    p_conser = models.FloatField(blank=True, null=True)
    ocupa_pred = models.CharField(max_length=254, blank=True, null=True)
    d_ocu = models.FloatField(blank=True, null=True)
    p_ocu = models.FloatField(blank=True, null=True)
    v_economic = models.FloatField(blank=True, null=True)
    c_horno = models.CharField(max_length=254, blank=True, null=True)
    d_c_horno = models.FloatField(blank=True, null=True)
    p_c_horno = models.FloatField(blank=True, null=True)
    disp_rrss_field = models.CharField(db_column='disp_rrss_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    d_disp_rrs = models.FloatField(blank=True, null=True)
    p_dis_rrss = models.FloatField(blank=True, null=True)
    disp_excre = models.CharField(max_length=254, blank=True, null=True)
    d_disp_exc = models.FloatField(blank=True, null=True)
    p_disp_exc = models.FloatField(blank=True, null=True)
    m_rrss_ind = models.CharField(max_length=254, blank=True, null=True)
    d_m_rrss_i = models.FloatField(blank=True, null=True)
    p_m_rrss = models.FloatField(blank=True, null=True)
    c_amb = models.CharField(max_length=254, blank=True, null=True)
    d_c_amb = models.FloatField(blank=True, null=True)
    p_c_amb = models.FloatField(blank=True, null=True)
    v_ambienta = models.FloatField(blank=True, null=True)
    v_v = models.FloatField(blank=True, null=True)
    niv_vulnerabilidad = models.CharField(max_length=15, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_caract_evar_vulnerabilidad'


class GisGeneCaminoQhapaqnan(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    fid_field = models.IntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    entity = models.CharField(max_length=-1, blank=True, null=True)
    layer = models.CharField(max_length=-1, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    linetype = models.CharField(max_length=-1, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    linewt = models.IntegerField(blank=True, null=True)
    refname = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_camino_qhapaqnan'


class GisGeneCuencasHidrograficasN8(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    cod_cu_n7 = models.CharField(max_length=10, blank=True, null=True)
    cod_cu_n8 = models.CharField(max_length=10, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_cuencas_hidrograficas_n8'


class GisGeneCuencasHidrograficasN9(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    gridcode = models.BigIntegerField(blank=True, null=True)
    nomb_cu_n7 = models.CharField(max_length=25, blank=True, null=True)
    cod_cu_n7 = models.CharField(max_length=15, blank=True, null=True)
    cod_cu_n8 = models.CharField(max_length=15, blank=True, null=True)
    cod_cu_n9 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_cuencas_hidrograficas_n9'


class GisGeneCurvasProvincia(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    layer = models.CharField(max_length=-1, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    closed_con = models.CharField(max_length=-1, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_curvas_provincia'


class GisGeneHabilitacionesUrbanas(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    gid = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    formal = models.CharField(max_length=-1, blank=True, null=True)
    resolucion = models.CharField(max_length=-1, blank=True, null=True)
    nro_plano = models.CharField(max_length=-1, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    area_total = models.FloatField(blank=True, null=True)
    recreacion = models.FloatField(blank=True, null=True)
    recre_por = models.FloatField(blank=True, null=True)
    educacion = models.FloatField(blank=True, null=True)
    educa_por = models.FloatField(blank=True, null=True)
    salud = models.FloatField(blank=True, null=True)
    salud_por = models.FloatField(blank=True, null=True)
    serpar = models.FloatField(blank=True, null=True)
    serpar_por = models.FloatField(blank=True, null=True)
    otro_fin = models.FloatField(blank=True, null=True)
    otro_fin_x = models.FloatField(blank=True, null=True)
    otro_uso = models.FloatField(blank=True, null=True)
    otro_uso_x = models.FloatField(blank=True, null=True)
    fore_arbo = models.FloatField(blank=True, null=True)
    fore_arb_x = models.FloatField(blank=True, null=True)
    area_verde = models.FloatField(blank=True, null=True)
    area_ver_1 = models.FloatField(blank=True, null=True)
    area_libre = models.FloatField(blank=True, null=True)
    area_lib_x = models.FloatField(blank=True, null=True)
    pro_alt_te = models.FloatField(blank=True, null=True)
    pr_altte_x = models.FloatField(blank=True, null=True)
    are_af_am_field = models.FloatField(db_column='are_af_am_', blank=True, null=True)  # Field renamed because it ended with '_'.
    are_af_a_1 = models.FloatField(blank=True, null=True)
    area_reser = models.FloatField(blank=True, null=True)
    area_res_1 = models.FloatField(blank=True, null=True)
    sube_elec = models.FloatField(blank=True, null=True)
    sube_elec_field = models.FloatField(db_column='sube_elec_', blank=True, null=True)  # Field renamed because it ended with '_'.
    zona_arq = models.FloatField(blank=True, null=True)
    zona_arq_x = models.FloatField(blank=True, null=True)
    faja_mar = models.FloatField(blank=True, null=True)
    faja_mar_x = models.FloatField(blank=True, null=True)
    reser = models.FloatField(blank=True, null=True)
    reser_por = models.FloatField(blank=True, null=True)
    observacio = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_habilitaciones_urbanas'


class GisGeneLineaAltaTensionElectrica(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    fid_field = models.BigIntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_linea_alta_tension_electrica'


class GisGeneLineaMediaTensionElectrica(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    codigosucu = models.CharField(max_length=-1, blank=True, null=True)
    codigotecn = models.CharField(max_length=-1, blank=True, null=True)
    codigote_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigotram = models.CharField(max_length=-1, blank=True, null=True)
    tiporedele = models.CharField(max_length=-1, blank=True, null=True)
    numerocond = models.IntegerField(blank=True, null=True)
    seccioncon = models.FloatField(blank=True, null=True)
    codigotais = models.CharField(max_length=-1, blank=True, null=True)
    codigoobra = models.CharField(max_length=-1, blank=True, null=True)
    fechainsta = models.DateField(blank=True, null=True)
    codpropiet = models.CharField(max_length=-1, blank=True, null=True)
    longitudre = models.FloatField(blank=True, null=True)
    fechacreac = models.DateField(blank=True, null=True)
    fechamodif = models.DateField(blank=True, null=True)
    tensionnom = models.FloatField(blank=True, null=True)
    codigotr_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigosecc = models.CharField(max_length=-1, blank=True, null=True)
    vnrrural = models.CharField(max_length=-1, blank=True, null=True)
    estadoda_1 = models.CharField(max_length=-1, blank=True, null=True)
    fechaest_2 = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_linea_media_tension_electrica'


class GisGenePdm2016Manzanas(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid_2 = models.IntegerField(blank=True, null=True)
    cod_distri = models.CharField(max_length=-1, blank=True, null=True)
    nomb_distr = models.CharField(max_length=-1, blank=True, null=True)
    cod_pdm = models.CharField(max_length=-1, blank=True, null=True)
    servicios = models.CharField(max_length=-1, blank=True, null=True)
    material = models.CharField(max_length=-1, blank=True, null=True)
    estado_con = models.CharField(max_length=-1, blank=True, null=True)
    uso_suelo = models.CharField(max_length=-1, blank=True, null=True)
    observacio = models.CharField(max_length=-1, blank=True, null=True)
    perimetro = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    fid_manzan = models.IntegerField(blank=True, null=True)
    fid_catast = models.IntegerField(blank=True, null=True)
    cod_dist_1 = models.CharField(max_length=-1, blank=True, null=True)
    nomb_dis_1 = models.CharField(max_length=-1, blank=True, null=True)
    observac_1 = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    mostrar = models.CharField(max_length=-1, blank=True, null=True)
    shape_le_1 = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdm_2016_manzanas'


class GisGenePdu2013BordeUrbano(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    gid = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_borde_urbano'


class GisGenePdu2013Equipamiento(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    gid = models.IntegerField(blank=True, null=True)
    zona = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_equipamiento'


class GisGenePdu2013FajaServidumbreEgensa(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    linea_codi = models.CharField(max_length=254, blank=True, null=True)
    orden = models.BigIntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_faja_servidumbre_egensa'


class GisGenePdu2013FajaViaFerrea(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    jerarquia = models.CharField(max_length=254, blank=True, null=True)
    estado_con = models.CharField(max_length=254, blank=True, null=True)
    tipo_pavim = models.CharField(max_length=254, blank=True, null=True)
    seccion_vi = models.CharField(max_length=254, blank=True, null=True)
    tipo_trans = models.CharField(max_length=254, blank=True, null=True)
    codigo = models.CharField(max_length=254, blank=True, null=True)
    observacio = models.CharField(max_length=254, blank=True, null=True)
    long_km = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    buff_dist = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_faja_via_ferrea'


class GisGenePdu2013ProteccionAmbiental(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    gid = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=-1, blank=True, null=True)
    tipo = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_proteccion_ambiental'


class GisGenePdu2013ZonificacionFull(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    gid = models.FloatField(blank=True, null=True)
    zona = models.CharField(max_length=254, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    hab_ha = models.CharField(max_length=50, blank=True, null=True)
    densidad = models.CharField(max_length=50, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_zonificacion_full'


class GisGenePdu2013Zpce(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    gid = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=254, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    propuesta = models.CharField(max_length=254, blank=True, null=True)
    nombre_1 = models.CharField(max_length=254, blank=True, null=True)
    tipo_1 = models.CharField(max_length=254, blank=True, null=True)
    nivel = models.CharField(max_length=50, blank=True, null=True)
    propuesta_field = models.CharField(db_column='propuesta_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'gis_gene_pdu_2013_zpce'


class GisGeneRedHidrografica(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    gid = models.FloatField(blank=True, null=True)
    rasgo_prin = models.CharField(max_length=-1, blank=True, null=True)
    rasgo_secu = models.CharField(max_length=-1, blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    provincia = models.CharField(max_length=-1, blank=True, null=True)
    orden = models.CharField(max_length=-1, blank=True, null=True)
    pfafstette = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_red_hidrografica'


class GisGeneSedacuscoBuzones(models.Model):
    geom = models.PointField(srid=32719, dim=3, blank=True, null=True)
    fid_field = models.IntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    entity = models.CharField(max_length=16, blank=True, null=True)
    layer = models.CharField(max_length=254, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    linetype = models.CharField(max_length=254, blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    linewt = models.IntegerField(blank=True, null=True)
    refname = models.CharField(max_length=254, blank=True, null=True)
    angle = models.FloatField(blank=True, null=True)
    mostrar = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_sedacusco_buzones'


class GisGeneSedacuscoRedAguaPotable(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    codidred = models.CharField(max_length=254, blank=True, null=True)
    d_tipo = models.CharField(max_length=254, blank=True, null=True)
    d_xdiametr = models.CharField(max_length=254, blank=True, null=True)
    d_xmateria = models.CharField(max_length=254, blank=True, null=True)
    d_yantigue = models.CharField(max_length=254, blank=True, null=True)
    d_yfechaca = models.CharField(max_length=254, blank=True, null=True)
    d_yprofund = models.CharField(max_length=254, blank=True, null=True)
    d_yreferen = models.CharField(max_length=254, blank=True, null=True)
    longitudre = models.FloatField(blank=True, null=True)
    red_zre = models.CharField(max_length=20, blank=True, null=True)
    mostrar = models.CharField(max_length=10, blank=True, null=True)
    red = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_sedacusco_red_agua_potable'


class GisGeneSedacuscoRedDesague(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    featid1 = models.FloatField(blank=True, null=True)
    antiguedad = models.CharField(max_length=254, blank=True, null=True)
    calle = models.CharField(max_length=254, blank=True, null=True)
    diametro = models.CharField(max_length=254, blank=True, null=True)
    idmicrosec = models.CharField(max_length=254, blank=True, null=True)
    idzona = models.CharField(max_length=254, blank=True, null=True)
    material = models.CharField(max_length=254, blank=True, null=True)
    observacio = models.CharField(max_length=254, blank=True, null=True)
    profundida = models.CharField(max_length=254, blank=True, null=True)
    referencia = models.CharField(max_length=254, blank=True, null=True)
    tipo = models.CharField(max_length=254, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    fecha_cata = models.CharField(max_length=254, blank=True, null=True)
    mostrar = models.CharField(max_length=10, blank=True, null=True)
    redes = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_sedacusco_red_desague'


class GisGeneSubestacionesDistribucionElectrica(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    codigoempr = models.CharField(max_length=-1, blank=True, null=True)
    codigosucu = models.CharField(max_length=-1, blank=True, null=True)
    nombresed = models.CharField(max_length=-1, blank=True, null=True)
    direccions = models.CharField(max_length=-1, blank=True, null=True)
    codigotipo = models.CharField(max_length=-1, blank=True, null=True)
    codpropiet = models.CharField(max_length=-1, blank=True, null=True)
    codigotecn = models.CharField(max_length=-1, blank=True, null=True)
    codigote_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigote_2 = models.CharField(max_length=-1, blank=True, null=True)
    codigoinei = models.CharField(max_length=-1, blank=True, null=True)
    codigoin_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigoin_2 = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigoobra = models.CharField(max_length=-1, blank=True, null=True)
    fechainsta = models.DateField(blank=True, null=True)
    codigoesta = models.CharField(max_length=-1, blank=True, null=True)
    codigooper = models.CharField(max_length=-1, blank=True, null=True)
    numerotraf = models.IntegerField(blank=True, null=True)
    codigomate = models.CharField(max_length=-1, blank=True, null=True)
    tensionpri = models.FloatField(blank=True, null=True)
    tensionsec = models.FloatField(blank=True, null=True)
    potenciain = models.FloatField(blank=True, null=True)
    demandamax = models.FloatField(blank=True, null=True)
    demandam_1 = models.FloatField(blank=True, null=True)
    cantidadci = models.IntegerField(blank=True, null=True)
    cantidadcl = models.IntegerField(blank=True, null=True)
    cantidad_1 = models.IntegerField(blank=True, null=True)
    cantidadla = models.IntegerField(blank=True, null=True)
    etiqueta = models.CharField(max_length=-1, blank=True, null=True)
    observacio = models.CharField(max_length=-1, blank=True, null=True)
    usuariocre = models.CharField(max_length=-1, blank=True, null=True)
    usuariomod = models.CharField(max_length=-1, blank=True, null=True)
    fechacreac = models.DateField(blank=True, null=True)
    fechamodif = models.DateField(blank=True, null=True)
    fecharepli = models.CharField(max_length=-1, blank=True, null=True)
    angulo = models.FloatField(blank=True, null=True)
    codigoeqpo = models.CharField(max_length=-1, blank=True, null=True)
    codigote_3 = models.CharField(max_length=-1, blank=True, null=True)
    codigosecc = models.CharField(max_length=-1, blank=True, null=True)
    codigotram = models.CharField(max_length=-1, blank=True, null=True)
    codigosed = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_2 = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_3 = models.CharField(max_length=-1, blank=True, null=True)
    cantidadti = models.IntegerField(blank=True, null=True)
    codigoti_4 = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_5 = models.CharField(max_length=-1, blank=True, null=True)
    cantidad_2 = models.IntegerField(blank=True, null=True)
    codigoti_6 = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_7 = models.CharField(max_length=-1, blank=True, null=True)
    cantidad_3 = models.IntegerField(blank=True, null=True)
    ultimafech = models.DateField(blank=True, null=True)
    codestadoa = models.CharField(max_length=-1, blank=True, null=True)
    codigoob_1 = models.CharField(max_length=-1, blank=True, null=True)
    etiquetaar = models.CharField(max_length=-1, blank=True, null=True)
    codlocalid = models.CharField(max_length=-1, blank=True, null=True)
    vnr = models.CharField(max_length=-1, blank=True, null=True)
    nroeqpopro = models.IntegerField(blank=True, null=True)
    vnrrural = models.CharField(max_length=-1, blank=True, null=True)
    nrovias1 = models.IntegerField(blank=True, null=True)
    nrovias2 = models.IntegerField(blank=True, null=True)
    nrovias3 = models.IntegerField(blank=True, null=True)
    nrovias4 = models.IntegerField(blank=True, null=True)
    codigoti_8 = models.CharField(max_length=-1, blank=True, null=True)
    codigoti_9 = models.CharField(max_length=-1, blank=True, null=True)
    codigot_10 = models.CharField(max_length=-1, blank=True, null=True)
    codigot_11 = models.CharField(max_length=-1, blank=True, null=True)
    codigoma_1 = models.CharField(max_length=-1, blank=True, null=True)
    codigotsop = models.CharField(max_length=-1, blank=True, null=True)
    codigots_1 = models.CharField(max_length=-1, blank=True, null=True)
    alturatsop = models.IntegerField(blank=True, null=True)
    alturats_1 = models.IntegerField(blank=True, null=True)
    cantidad_4 = models.IntegerField(blank=True, null=True)
    cantidad_5 = models.IntegerField(blank=True, null=True)
    cantidad_6 = models.IntegerField(blank=True, null=True)
    cantidad_7 = models.IntegerField(blank=True, null=True)
    codigocp = models.CharField(max_length=-1, blank=True, null=True)
    nombrecp = models.CharField(max_length=-1, blank=True, null=True)
    estadodata = models.CharField(max_length=-1, blank=True, null=True)
    fechaestad = models.DateField(blank=True, null=True)
    tipoacceso = models.IntegerField(blank=True, null=True)
    codigoes_1 = models.IntegerField(blank=True, null=True)
    fechaest_1 = models.DateField(blank=True, null=True)
    imagen = models.IntegerField(blank=True, null=True)
    fechaultim = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar1 = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar2 = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar3 = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar4 = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar5 = models.CharField(max_length=-1, blank=True, null=True)
    auxiliar6 = models.CharField(max_length=-1, blank=True, null=True)
    fechaejecu = models.DateField(blank=True, null=True)
    globalid = models.CharField(max_length=-1, blank=True, null=True)
    observac_1 = models.CharField(max_length=-1, blank=True, null=True)
    estadoda_1 = models.CharField(max_length=-1, blank=True, null=True)
    fechaest_2 = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_gene_subestaciones_distribucion_electrica'


class GisPropAmbFranjaProteccionRecursoHidrico(models.Model):
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    ga = models.CharField(max_length=200, blank=True, null=True)
    een = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_franja_proteccion_recurso_hidrico'


class GisPropAmbReforestacion(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_reforestacion'


class GisPropAmbRestauracion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    proyecto = models.CharField(max_length=50, blank=True, null=True)
    cod = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo_restauracion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_restauracion'


class GisPropAmbZiere(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    zre = models.CharField(max_length=5, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    proyecto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_ziere'


class GisPropAmbZonaProteccionConservacionEcologica(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_zona_proteccion_conservacion_ecologica'


class GisPropAmbZonaProteccionRecursoHidrico(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=10, blank=True, null=True)
    ga = models.CharField(max_length=20, blank=True, null=True)
    een = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_amb_zona_proteccion_recurso_hidrico'


class GisPropFcAreasVerdes(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_areas_verdes'


class GisPropFcEspaciosPublicosPolygon(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    uso = models.CharField(max_length=25, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_espacios_publicos_polygon'


class GisPropFcEspaciosPublicosPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32719, dim=3, blank=True, null=True)
    uso = models.CharField(max_length=200, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_espacios_publicos_polyline'


class GisPropFcManzanas(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    numero = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_manzanas'


class GisPropFcPuntos(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_puntos'


class GisPropFcSistemaVial(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id_via = models.CharField(max_length=13, blank=True, null=True)
    nomb_via = models.CharField(max_length=200, blank=True, null=True)
    tipo_via = models.CharField(max_length=50, blank=True, null=True)
    codi_via = models.CharField(max_length=6, blank=True, null=True)
    toponimia = models.CharField(max_length=35, blank=True, null=True)
    cuadra = models.CharField(max_length=6, blank=True, null=True)
    ubicación = models.CharField(max_length=50, blank=True, null=True)
    jerarquia_field = models.CharField(db_column='jerarquia_', max_length=50, blank=True, null=True)  # Field renamed because it ended with '_'.
    pendiente = models.CharField(max_length=50, blank=True, null=True)
    pendient_1 = models.CharField(max_length=50, blank=True, null=True)
    e_conserva = models.CharField(max_length=50, blank=True, null=True)
    tipo_pavim = models.CharField(max_length=50, blank=True, null=True)
    accesibili = models.CharField(max_length=50, blank=True, null=True)
    transitabi = models.CharField(max_length=50, blank=True, null=True)
    acera = models.CharField(max_length=50, blank=True, null=True)
    alineamien = models.CharField(max_length=50, blank=True, null=True)
    ancho = models.CharField(max_length=10, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    mostrar = models.CharField(max_length=10, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    rango = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_sistema_vial'


class GisPropFcSistemaVialNodos(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    fid_field = models.BigIntegerField(db_column='fid_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    nodo = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_sistema_vial_nodos'


class GisPropFcSistemaVialSecciones(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    corte = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    vert_1 = models.CharField(max_length=5, blank=True, null=True)
    vert_2 = models.CharField(max_length=5, blank=True, null=True)
    url_image = models.CharField(max_length=255, blank=True, null=True)
    cod_corte = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_sistema_vial_secciones'


class GisPropFcSistemaVialSeccionesVertices(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PointField(srid=32719, blank=True, null=True)
    corte = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    vert_1 = models.CharField(max_length=5, blank=True, null=True)
    vert_2 = models.CharField(max_length=5, blank=True, null=True)
    vertex_index = models.IntegerField(blank=True, null=True)
    vertex_part = models.IntegerField(blank=True, null=True)
    vertex_part_index = models.IntegerField(blank=True, null=True)
    distance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    angle = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_sistema_vial_secciones_vertices'


class GisPropFcViaPavimentacion(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    admapkey = models.BigIntegerField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_via_pavimentacion'


class GisPropFcViasDet(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=3, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_vias_det'


class GisPropFcZonificacion(models.Model):
    geom = models.MultiPolygonField(srid=32719, dim=4, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    objectid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zona = models.CharField(max_length=50, blank=True, null=True)
    sub_zona = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    id_manzana = models.CharField(max_length=50, blank=True, null=True)
    id_agrupac = models.CharField(max_length=50, blank=True, null=True)
    descripcio = models.CharField(max_length=254, blank=True, null=True)
    id_agrup_1 = models.CharField(max_length=15, blank=True, null=True)
    zonificaci = models.CharField(max_length=15, blank=True, null=True)
    descripc_1 = models.CharField(max_length=254, blank=True, null=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    frente_min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lote_min = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coefi_edif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    area_libre = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altura = models.CharField(max_length=10, blank=True, null=True)
    densidad = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plan_refer = models.CharField(max_length=50, blank=True, null=True)
    agrupacion = models.CharField(max_length=254, blank=True, null=True)
    tipo_agrup = models.CharField(max_length=254, blank=True, null=True)
    orig_fid = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ajust_spa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_zonificacion'


class GisPropFcZonificacionVertices(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    punto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_fc_zonificacion_vertices'


class GisPropGrdEstructurasPolygon(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_estructuras_polygon'


class GisPropGrdEstructurasPolyline(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    longitud = models.FloatField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_estructuras_polyline'


class GisPropGrdEstructurasSecciones(models.Model):
    geom = models.MultiLineStringField(srid=32719, blank=True, null=True)
    id_field = models.IntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    corte = models.CharField(max_length=30, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)
    cod_corte = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_estructuras_secciones'


class GisPropGrdFajaMarginalRio(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_faja_marginal_rio'


class GisPropGrdFranjaAislamientoSeguridad(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_franja_aislamiento_seguridad'


class GisPropGrdFranjaProteccion(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    franja = models.CharField(max_length=-1, blank=True, null=True)
    zonificacion = models.CharField(max_length=-1, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_franja_proteccion'


class GisPropGrdFranjaSecciones(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    wkb_geometry = models.MultiLineStringField(srid=32719, blank=True, null=True)
    seccion = models.CharField(max_length=20, blank=True, null=True)
    codigo_zre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_franja_secciones'


class GisPropGrdFranjaVertices(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    franja = models.CharField(max_length=-1, blank=True, null=True)
    coord_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)
    hito = models.CharField(max_length=-1, blank=True, null=True)
    wkb_geometry = models.PointField(srid=32719, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_franja_vertices'


class GisPropGrdNoEstrucFranjaAislamVertices(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    hito = models.BigIntegerField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    nomb_franja = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_no_estruc_franja_aislam_vertices'


class GisPropGrdNoEstrucFranjaProtecVertices(models.Model):
    geom = models.PointField(srid=32719, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    id_field = models.BigIntegerField(db_column='id_', blank=True, null=True)  # Field renamed because it ended with '_'.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    hito = models.BigIntegerField(blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_no_estruc_franja_protec_vertices'


class GisPropGrdNoEstructuralesPolygon(models.Model):
    geom = models.MultiPolygonField(srid=32719, blank=True, null=True)
    codigo_zre = models.CharField(max_length=15, blank=True, null=True)
    tipo = models.CharField(max_length=200, blank=True, null=True)
    georeferen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gis_prop_grd_no_estructurales_polygon'


class PortalSlide(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'portal_slide'


class PortalSlideitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    slide = models.ForeignKey(PortalSlide, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_slideitem'


class TZona(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_zona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=20, decimal_places=10)
    lng = models.DecimalField(max_digits=20, decimal_places=10)
    zoom = models.DecimalField(max_digits=20, decimal_places=10)
    observacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_zona'


class WorldAmbitos(models.Model):
    id = models.BigAutoField(primary_key=True)
    objectid = models.BigIntegerField()
    admapkey = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'world_ambitos'


class WorldAmbitosutm(models.Model):
    id = models.BigAutoField(primary_key=True)
    objectid = models.BigIntegerField()
    admapkey = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=32719)

    class Meta:
        managed = False
        db_table = 'world_ambitosutm'


class WorldComarca(models.Model):
    id = models.BigAutoField(primary_key=True)
    admapkey = models.BigIntegerField()
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'world_comarca'


class WorldFriend(models.Model):
    id = models.BigAutoField(primary_key=True)
    nick_name = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    likes = models.CharField(max_length=250)
    dob = models.DateField()
    live_in = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_friend'


class WorldSourcewms(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    visible = models.BooleanField()
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'world_sourcewms'


class WorldWorldborder(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    fips = models.CharField(max_length=2, blank=True, null=True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'world_worldborder'


class ZonasZony(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'zonas_zony'
