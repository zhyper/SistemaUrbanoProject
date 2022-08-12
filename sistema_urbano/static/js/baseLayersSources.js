 //SOURCES----------------------------------------------------------------------------------


 const zpaPDU2013Source = new ol.source.ImageWMS({
   url: urlGeoserver,
   //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
   params: {
     LAYERS: 'sgotp-41zre:gis_gene_pdu_2013_proteccion_ambiental',
     TILED: true,
     //'STYLES': 'pdu_2013_zpa',
     //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
     //'FORMAT_OPTIONS': 'antialias:none'
   },
   serverType: 'geoserver',
   crossOrigin: "anonymous",
   // Countries have transparency, so do not fade tiles:
   //transition: 0,
 })

 const zonasWmsSource = new ol.source.ImageWMS({
   url: urlGeoserver,
   params: { 'LAYERS': 'sgotp-41zre:gis_base_zonas_zre_v2', 'TILED': true },
   serverType: 'geoserver',
   crossOrigin: "anonymous",
   //transition: 0,
 });

 const habiliWmsSource = new  ol.source.ImageWMS({
   url: urlGeoserver,
   //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
   params: {
     LAYERS: 'sgotp-41zre:gis_gene_habilitaciones_urbanas',
     TILED: true,
     
     //'STYLES': 'habilitaciones_urbanas_polyline',
     //'FORMAT_OPTIONS': 'antialias:none'
   },
   serverType: 'geoserver',
   crossOrigin: "anonymous",
   // Countries have transparency, so do not fade tiles:
   //transition: 0,
 })

 const manzanas41ZREWmsSource = new ol.source.ImageWMS({
   url: urlGeoserver,
   //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
   params: {
     LAYERS: 'sgotp-41zre:gis_carac_fc_manzanas',
     TILED: true,
     //'STYLES': 'manzanas_polygon',
     //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
   },
   serverType: 'geoserver',
   crossOrigin: "anonymous",
   
   // Countries have transparency, so do not fade tiles:
   //transition: 0,
 })

 const lotes41ZREWmsSource = new ol.source.ImageWMS({
   url: urlGeoserver,
   //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
   params: {
     LAYERS: 'sgotp-41zre:gis_carac_fc_lotes',
     TILED: true,
     //'STYLES': 'manzanas_polygon',
     //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
   },
   serverType: 'geoserver',
   crossOrigin: "anonymous",
   // Countries have transparency, so do not fade tiles:
   //transition: 0,
 })


 // Sources para la optención de Informacion API REST
 // GetFeatureInfo:
 

 const zonificacionPDU2013Source = new ol.source.ImageWMS({
  // url: urlGeoserver,
  url: urlGeoserver,
  //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
  params: {
    LAYERS: 'sgotp-41zre:gis_gene_pdu_2013_zonificacion_full',
    TILED: true,
    //'STYLES': 'pdu_2013_zpa',
    //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
    //'FORMAT_OPTIONS': 'antialias:none'
  },
  serverType: 'geoserver',
  // Countries have transparency, so do not fade tiles:
  //transition: 0,
})


   WMSSources.push(zpaPDU2013Source);
   WMSSources.push(zonasWmsSource)
   WMSSources.push(habiliWmsSource)
   WMSSources.push(manzanas41ZREWmsSource)
   WMSSources.push(lotes41ZREWmsSource)
   WMSSources.push(zonificacionPDU2013Source)