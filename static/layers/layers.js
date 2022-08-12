var wms_layers = [];

var lyr_gis_carac_fc_ambito_0 = new ol.layer.Image({
  source: new ol.source.ImageWMS({
    url: "http://localhost/geoserver/sgotp-41zre/wms",
    attributions: [new ol.Attribution({ html: '<a href=""></a>' })],
    params: {
      LAYERS: "gis_carac_fc_ambito",
      TILED: "true",
      VERSION: "1.3.0",
    },
  }),
  title: "gis_carac_fc_ambito",
  opacity: 1.0,
});

wms_layers.push([lyr_gis_carac_fc_ambito_0, 1]);




var lyr_gis_carac_fc_manzanas_1 = new ol.layer.Image({
  source: new ol.source.ImageWMS({
    url: "http://localhost/geoserver/sgotp-41zre/wms",
    attributions: [new ol.Attribution({ html: '<a href=""></a>' })],
    params: {
      LAYERS: "gis_carac_fc_manzanas",
      TILED: "true",
      VERSION: "1.3.0",
    },
  }),
  title: "gis_carac_fc_manzanas",
  opacity: 1.0,
});
wms_layers.push([lyr_gis_carac_fc_manzanas_1, 1]);


var lyr_gis_carac_fc_lotes_2 = new ol.layer.Image({
  source: new ol.source.ImageWMS({
    url: "http://localhost/geoserver/sgotp-41zre/wms",
    attributions: [new ol.Attribution({ html: '<a href=""></a>' })],
    params: {
      LAYERS: "gis_carac_fc_lotes",
      TILED: "true",
      VERSION: "1.3.0",
    },
  }),
  title: "gis_carac_fc_lotes",
  opacity: 1.0,
});
wms_layers.push([lyr_gis_carac_fc_lotes_2, 1]);

var lyr_gis_gene_habilitaciones_urbanas_3 = new ol.layer.Image({
  source: new ol.source.ImageWMS({
    url: "http://localhost/geoserver/sgotp-41zre/wms",
    attributions: [new ol.Attribution({ html: '<a href=""></a>' })],
    params: {
      LAYERS: "gis_gene_habilitaciones_urbanas",
      TILED: "true",
      VERSION: "1.3.0",
    },
  }),
  title: "gis_gene_habilitaciones_urbanas",
  opacity: 1.0,
});
wms_layers.push([lyr_gis_gene_habilitaciones_urbanas_3, 1]);

lyr_gis_carac_fc_ambito_0.setVisible(true);
lyr_gis_carac_fc_manzanas_1.setVisible(true);
lyr_gis_carac_fc_lotes_2.setVisible(true);
lyr_gis_gene_habilitaciones_urbanas_3.setVisible(true);
var layersList = [
  lyr_gis_carac_fc_ambito_0,
  lyr_gis_carac_fc_manzanas_1,
  lyr_gis_carac_fc_lotes_2,
  lyr_gis_gene_habilitaciones_urbanas_3,
];
