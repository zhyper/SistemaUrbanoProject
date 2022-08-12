// Base Layers:----------------------------------------------------------------------------

var baseLayers = new ol.layer.Group({
  title: "Base Layers",
  openInLayerSwitcher: false,
  layers: [
    new ol.layer.Tile({
      title: "Watercolor",
      baseLayer: true,
      visible: false,
      source: new ol.source.Stamen({ layer: "watercolor" }),
    }),
    new ol.layer.Tile({
      title: "Toner",
      baseLayer: true,
      visible: false,
      source: new ol.source.Stamen({ layer: "toner" }),
    }),
    new ol.layer.Tile({
      title: "OSM",
      baseLayer: true,
      source: new ol.source.OSM(),
      visible: false,
    }),
    //definiendo los BASEMAPS
    // :0
    new ol.layer.Tile({
      title: "Blank",
      baseLayer: true,
      visible: false,
      //source: null,
      source: new ol.source.XYZ({
        //url: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWNgYGD4DwABBAEAHnOcQAAAAABJRU5ErkJggg==', //black
        url: "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==", //white
      }),
    }),
    // :1
    new ol.layer.Tile({
      title: "Google Map Hybrid",
      baseLayer: true,
      visible: true,
      // Again set this layer as a base layer
      //visible: true,
      source: new ol.source.XYZ({
        url: "http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}",
      }),
    }),
  ],
});

var baseLayerPDU2013 = new ol.layer.Group({
  //properties: {
  title: "PDU 2013-2023",
  openInLayerSwitcher: false,
  //},
  layers: [
    /**  ZONIFICACION PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "Zonificación",
      //openInLayerSwitcher: false,
      //baseLayer: true,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: false,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_pdu_2013_zonificacion_full",
          TILED: true,
          STYLES: "pdu_zonificacion_full",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:none",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),
    /** ZPA PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "ZPA",
      //baseLayer: true,
      //openInLayerSwitcher: false,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: false,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_pdu_2013_proteccion_ambiental",
          TILED: true,
          STYLES: "pdu_2013_zpa",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:none",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),
    /** ZPCE PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "ZPCE",
      //openInLayerSwitcher: false,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: false,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_pdu_2013_zpce",
          TILED: true,
          STYLES: "pdu_2013_zpce",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:none",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),
    /**  RED HIDRICA PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "Red Hídrica",
      //openInLayerSwitcher: false,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      //visible:true,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_red_hidrografica",
          TILED: true,
          STYLES: "pdu_red_hidrica",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:text",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),

    /**  FAJA DE DERVIDUMBRE EGEMSA PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "Faja de Servidumbre EGEMSA",
      //openInLayerSwitcher: false,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: true,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_pdu_2013_faja_servidumbre_egensa",
          TILED: true,
          STYLES: "pdu_2013_faja_servidumbre_egemsa",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:none",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),

    /**  FAJA VIA FERREA PDU 2013-2023 */
    new ol.layer.Image({
      //properties: {
      title: "Faja Vía Férrea",
      //openInLayerSwitcher: false,
      //},
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: true,
      source: new ol.source.ImageWMS({
        url: urlGeoserver,
        //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
        params: {
          LAYERS: "sgotp-41zre:gis_gene_pdu_2013_faja_via_ferrea",
          TILED: true,
          STYLES: "pdu_faja_via_ferrea",
          //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          FORMAT_OPTIONS: "antialias:none",
        },
        serverType: "geoserver",
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),
    //BORDE - URBANO - PDU
    new ol.layer.Image({
        title: 'Borde Urbano 2013',
        visible:true,
        source: new ol.source.ImageWMS({
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_gene_pdu_2013_borde_urbano',
            TILED: true,
            'STYLES': 'borde_urbano_polygon',
            //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
  ],
});


//****************************************************************************
// LAYERS CARACTERIZACION ----------------------------------------------------
//****************************************************************************

var baseLayer41ZRECarac = new ol.layer.Group({
    //properties: {
      title: '41ZRE Caracterización',
      openInlayerSwitcher: true
    //}
    ,
    layers: [

      //  AMBIENTAL CARACTERIZACION ---------------------------------------------
      new ol.layer.Group({
        title: 'AMBIENTAL',
        openInLayerSwitcher: false,
        layers: [
          new ol.layer.Image({
            properties: {
              title: 'Cobertura Vegetal'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_cobertura_vegetal',
                TILED: true,
                'STYLES': 'amb_cobertura_vegetal',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Areas Críticas de Acumulación RRSS'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_areas_criticas_acumulacion_rrss',
                TILED: true,
                'STYLES': 'gis_carac_amb_areas_criticas_acumulacion_rrss_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Ecosistemas y Espacios Naturales'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_een',
                TILED: true,
                'STYLES': 'gis_carac_amb_een_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Grado de Antropización'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_ga',
                TILED: true,
                'STYLES': 'gis_carac_amb_ga_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Manantiales'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_manantiales',
                TILED: true,
                'STYLES': 'gis_carac_amb_manantiales_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Puntos de quema RRSS'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_puntos_quema_rrss',
                TILED: true,
                'STYLES': 'gis_carac_amb_puntos_quema_rrss_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Puntos de vertimiento'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_puntos_vertimiento',
                TILED: true,
                'STYLES': 'gis_carac_amb_puntos_vertimiento_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Zonas de Protección Ambiental'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_zona_proteccion_ambiental',
                TILED: true,
                'STYLES': 'gis_carac_amb_zpa_zona_proteccion_ambiental_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),

          new ol.layer.Image({
            properties: {
              title: 'Zonas de Protecc. Conserv. Ecologica ZPCE',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_zpce_zonas_proteccion_conservacion_ecologica',
                TILED: true,
                'STYLES': 'gis_carac_amb_zpce_zonas_proteccion_conservacion_ecologica_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),

          new ol.layer.Image({
            properties: {
              title: 'Concesiones Mineras',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_amb_concesiones_mineras',
                TILED: true,
                'STYLES': 'gis_carac_amb_concesiones_mineras_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        ]
      },
      ),

      //  FISICO CONSTRUIDO CARACTERIZACION ---------------------------------------------
      new ol.layer.Group({
        title: 'FISICO CONSTRUIDO',
        openInLayerSwitcher: false,
        layers: [
          new ol.layer.Image({
            properties: {
              title: 'Linea Vía Férrea'
            },
            visible: true,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_linea_ferrea',
                TILED: true,
                'STYLES': 'gis_carac_fc_linea_ferrea_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Areas de aporte'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_gene_pdu_2013_zonificacion_full',
                TILED: true,
                'STYLES': 'pdu_zonificacion_areas_de_aporte_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Jerarquía Vial'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_sistema_vial',
                TILED: true,
                'STYLES': 'gis_carac_fc_sistema_vial_jerarquia_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Pendiente Vial'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_sistema_vial',
                TILED: true,
                'STYLES': 'gis_carac_fc_sistema_vial_pendiente_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Tipo pavimento Vial'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_sistema_vial',
                TILED: true,
                'STYLES': 'gis_carac_fc_sistema_vial_tipo_pavimento_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Estado conservación Vial'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_sistema_vial',
                TILED: true,
                'STYLES': 'gis_carac_fc_sistema_vial_estado_conservacion_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        
          new ol.layer.Image({
            properties: {
              title: 'Bloques C. 1N: Uso Predom.'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_bloques_1n',
                TILED: true,
                'STYLES': 'gis_carac_fc_bloques_1n_uso_predom_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        
          // :33
          new ol.layer.Image({
            properties: {
              title: 'Lotes Uso de Suelo'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_lotes',
                TILED: true,
                'STYLES': 'gis_carac_fc_lotes_uso_suelo_style',
                'FORMAT_OPTIONS': 'antialias:text'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        
          // :33
          new ol.layer.Image({
            properties: {
              title: 'Lotes'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_lotes',
                TILED: true,
                'STYLES': 'gis_carac_fc_lotes_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          
          // :34
          new ol.layer.Image({
            properties: {
              title: 'Manzanas'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_manzanas',
                TILED: true,
                'STYLES': 'gis_carac_fc_manzanas_style',
                'FORMAT_OPTIONS': 'antialias:text'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          // :34
          new ol.layer.Image({
            properties: {
              title: 'Secciones de Vía'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_fc_sistema_vial_secciones',
                TILED: true,
                'STYLES': 'gis_prop_fc_sistema_vial_secciones_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        ]

      }),

      //  GESTION DE RIESGO DE DESASTRES -----------------------------------------------------

      new ol.layer.Group({
        title: 'GESTION DE RIESGOS DE DESASTRES',
        openInLayerSwitcher: false,
        layers: [

          new ol.layer.Image({
            properties: {
              title: 'Peligros'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_grd_peligros',
                TILED: true,
                'STYLES': 'gis_carac_grd_peligros_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Riesgos'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_grd_riesgos',
                TILED: true,
                'STYLES': 'gis_carac_grd_riesgos_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Vulnerabilidad'
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
  
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_carac_grd_vulnerabilidad',
                TILED: true,
                'STYLES': 'gis_carac_grd_vulnerabilidad_style',
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          
        ],
      }),



    ]
  })

  //****************************************************************************
  // LAYERS PROPUESTA ----------------------------------------------------------
  //****************************************************************************

  var baseLayer41ZREProp = new ol.layer.Group({
    //properties: {
      title: '41ZRE Propuesta',
      openInLayerSwitcher: false,
    //}
    layers: [

      new ol.layer.Group({
        title: 'AMBIENTAL',
        openInLayerSwitcher: false,
        layers: [
          new ol.layer.Layer({
            properties: {
              title: 'ZPCE',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_zona_proteccion_conservacion_ecologica',
                TILED: true,
                'STYLES': 'gis_prop_amb_zona_proteccion_conservacion_ecologica_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),

          new ol.layer.Image({
            properties: {
              title: 'ZPCE: Borde: Especies',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_zpce_borde_especies',
                TILED: true,
                'STYLES': 'gis_prop_amb_zpce_borde_especies_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
  
          new ol.layer.Image({
            properties: {
              title: 'Zonas Productivas de Uso Sostenible',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_zonas_prod_uso_soste_zpus',
                TILED: true,
                'STYLES': 'gis_prop_amb_zonas_prod_uso_soste_zpus_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Zonas Protección del Recurso Hídrico',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_zona_proteccion_recurso_hidrico',
                TILED: true,
                'STYLES': 'gis_prop_amb_zona_proteccion_recurso_hidrico_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
  
          new ol.layer.Image({
            properties: {
              title: 'ZIERE',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_ziere',
                TILED: true,
                'STYLES': 'gis_prop_amb_ziere_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Reforestación',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_amb_reforestacion',
                TILED: true,
                'STYLES': 'gis_prop_amb_reforestacion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        ]
      }),

      new ol.layer.Group({
        properties: {
          title: 'FISICO CONSTRUIDO',
          openInLayerSwitcher: false,
        },
        layers: [
          new ol.layer.Image({
            properties: {
              title: 'Pavimentación de Vías',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_via_pavimentacion',
                TILED: true,
                'STYLES': 'gis_prop_fc_via_pavimentacion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                'FORMAT_OPTIONS': 'antialias:none'
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Zonificación 41ZRE',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_zonificacion',
                TILED: true,
                'STYLES': 'gis_prop_fc_zonificacion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                // 'FORMAT_OPTIONS': 'antialias:none',
                'FORMAT_OPTIONS': 'antialias:text',
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Trazo y Replanteo de Manzanas',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_replanteo_manzanas',
                TILED: true,
                'STYLES': 'gis_prop_fc_replanteo_manzanas_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                // 'FORMAT_OPTIONS': 'antialias:none',
                'FORMAT_OPTIONS': 'antialias:text',
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Trazo y Replanteo de Manzanas (vértices})',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_replanteo_manzanas_vertices',
                TILED: true,
                'STYLES': 'gis_prop_fc_replanteo_manzanas_vertices_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                // 'FORMAT_OPTIONS': 'antialias:none',
                'FORMAT_OPTIONS': 'antialias:text',
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Equipamiento - urbano 2',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_equipamiento_polygon',
                TILED: true,
                'STYLES': 'gis_prop_fc_equipamiento_polygon_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                'FORMAT_OPTIONS': 'antialias:text'
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Equipamiento - urbano 1',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_equipamiento_polyline',
                TILED: true,
                'STYLES': 'gis_prop_fc_equipamiento_polyline_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                'FORMAT_OPTIONS': 'antialias:text'
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: '(vértices) Zonificación 41ZRE',
            },
            visible:false,
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_zonificacion_vertices',
                TILED: true,
                'STYLES': 'gis_prop_fc_zonificacion_vertices_style',
                //'cql_filter': "codigo_zre ='" + this.codigo +"'",
                'FORMAT_OPTIONS': 'antialias:text'
                //'cql_filter': "codigo_zre ='" + this.infoZona_autostart.codigo_zona +"'",
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: "Sistema Vial"
            },
            visible:false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_sistema_vial',
                TILED: true,
                'STYLES': 'gis_prop_fc_sistema_vial_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: "Sistema Vial Nodos"
            },
            visible:false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              //url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_sistema_vial_nodos',
                TILED: true,
                'STYLES': 'gis_prop_fc_sistema_vial_nodos_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: "Secciones de Vías"
            },
            visible:false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_fc_sistema_vial_secciones',
                TILED: true,
                'STYLES': 'gis_prop_fc_sistema_vial_secciones_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        ]
        
      }),
      new ol.layer.Group({
        properties: {
          title: 'GESTION DE RIESGOS DE DESASTRES',
          openInlayerSwitcher: false
        },
        layers: [
          new ol.layer.Image({
            properties: {
              title: 'Dique de retencion de sedim. gavión',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_dique_reten_sedim_gavion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Canal de evac. de Aguas pluviales',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_canal_evac_aguas_pluv_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Cuneta de evac. de Aguas pluviales',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_cuneta_evac_aguas_pluviales_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Sub Drenes',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_drenes_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Limpieza de canal existente',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_limpieza_canal_exist_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Conformación de superficie de terreno',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_conforma_superf_terre_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Perfilado de superficie de terreno',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_perfilado_terre_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Muro de contención de Gavión',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_muro_conten_gavion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Línea de Gavión',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_linea_gavion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Geomanta de control erosional',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_geom_ctrl_eros_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Trincheras de madera',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_trincheras_madera_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Muro concreto armado tipo voladizo',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_mur_concre_arm_tipo_volad_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Muro concreto tipo ciclopeo',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polyline',
                TILED: true,
                'STYLES': 'gis_prop_grd_estru_muro_concreto_tipo_ciclopeo_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Franja de Protección de Peligro',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estructurales_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estructurales_franja_proteccion_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: '(vértices) Franja de Protección de Peligro',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estruc_franja_protec_vertices',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estruc_franja_protec_vertices_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Franja de Aislamiento de Seguridad',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estructurales_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estructurales_franja_aislamiento_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: '(vértices) Franja de Aislamiento',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estruc_franja_aislam_vertices',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estruc_franja_aislam_vertices_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Zona Intangible',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estructurales_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estructurales_zona_intangible_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          
          new ol.layer.Image({
            properties: {
              title: 'Lotes en Riesgo No Mitigable',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_no_estructurales_polygon',
                TILED: true,
                'STYLES': 'gis_prop_grd_no_estructurales_riesgo_no_mitigable_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Conformación de Terreno con Banquetas',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'grd_prop_estructurales_conforma_suelo_banquetas_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          new ol.layer.Image({
            properties: {
              title: 'Canalización de Aguas Pluviales I',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_polygon',
                TILED: true,
                'STYLES': 'grd_prop_estructurales_canal_evac_aguas_pluviales_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
          
          new ol.layer.Image({
            properties: {
              title: 'Secciones Propuestas Estructurales',
            },
            visible: false,
            //title: 'Inmebles Relig. Bloques 1er Nivel',
            source: new ol.source.ImageWMS({
              // url: urlGeoserver,
              url: urlGeoserver,
              //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
              params: {
                LAYERS: 'sgotp-41zre:gis_prop_grd_estructuras_secciones',
                TILED: true,
                'STYLES': 'gis_prop_grd_estructuras_secciones_style',
                //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
              },
              serverType: 'geoserver',
              // Countries have transparency, so do not fade tiles:
              //transition: 0,
            }),
          }),
        ]

      })

    ]
  })



  var baseLayer41ZREBase = new ol.layer.Group({
    //properties: {
      title: '41ZRE Base',
      openInLayerSwitcher: false,
    //},
    layers: [
     

      /**  RED HIDRICA PDU 2013-2023 */
      new ol.layer.Image({
        properties: {
          title: 'Red Hídrica',
          //openInLayerSwitcher: false,
        },
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        //visible:true,
        source: new ol.source.ImageWMS({
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_gene_red_hidrografica',
            TILED: true,
            'STYLES': 'pdu_red_hidrica',
            //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
            'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      new ol.layer.Image({
        properties: {
          title: 'Puntos Geodésicos 41ZRE',
          //openInLayerSwitcher: false,
        },
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        //visible:true,
        visible: false,
        source: new ol.source.ImageWMS({
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_carac_geo_puntos_geodesicos_41zre',
            TILED: true,
            'STYLES': 'gis_carac_geo_puntos_geodesicos_41zre_style',
            //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
            'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      new ol.layer.Image({
        properties: {
          title: 'Ambitos ZREs'
        },
        visible: true,
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        source: new ol.source.ImageWMS({
          //url: urlGeoserver,
          url: urlGeoserver,
          // url: 'http://144.91.84.249/geoserver/wms',
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_base_zonas_ambitos_v2',
            TILED: true,
            'STYLES': 'zona_ambito',
            //'cql_filter': "codigo_zre ='" + this.codigo+ "'"
            'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      new ol.layer.Image({
        properties: {
          title: 'ZREs'
        },
        visible: true,
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        source: new ol.source.ImageWMS({
          // url: urlGeoserver,
          url: urlGeoserver,
          // url: 'http://144.91.84.249/geoserver/wms',
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_base_zonas_zre_v2',
            TILED: true,
            'STYLES': 'zona_polygon_0',
            'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      new ol.layer.Image({
        properties: {
          title: 'ZREs (vertices)'
        },
        visible: false,
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        source: new ol.source.ImageWMS({
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_base_zonas_zre_vertices',
            TILED: true,
            'STYLES': 'gis_base_zonas_zre_vertices_style',
            'FORMAT_OPTIONS': 'antialias:text'

          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      new ol.layer.Image({
        properties: {
          title: 'ZRE Ambitos (vertices)'
        },
        visible: false,
        //title: 'Inmebles Relig. Bloques 1er Nivel',
        source: new ol.source.ImageWMS({
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_base_zonas_ambitos_vertices',
            TILED: true,
            'STYLES': 'gis_base_zonas_ambitos_vertices_style',
            'FORMAT_OPTIONS': 'antialias:text'

          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      
      /*** HBAILITACIONES URBANAS */
      new ol.layer.Image({
        properties:{
          title: 'Agrupaciones Urbanas',

        },
        visible: false,
        source: new ol.source.ImageWMS({
          // url: urlGeoserver,
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_gene_habilitaciones_urbanas',
            TILED: true,
            'STYLES': 'habilitaciones_urbanas_polyline',
            //'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),
      
      new ol.layer.Image({
        properties:{
          title: '(PDU) Limites Distritales Cusco',

        },
        visible: true,
        source: new ol.source.ImageWMS({
          // url: urlGeoserver,
          url: urlGeoserver,
          //params: {'LAYERS': URL_WS_V2+'sectores','STYLES': 'cat_sectores_only_label_sld', 'TILED': true},
          params: {
            LAYERS: 'sgotp-41zre:gis_base_limites_distritales_pdu_2013_polyline',
            TILED: true,
            'STYLES': 'gis_base_limites_distritales_ign_2022_style',
            'FORMAT_OPTIONS': 'antialias:text'
          },
          serverType: 'geoserver',
          // Countries have transparency, so do not fade tiles:
          //transition: 0,
        }),
      }),

    ]
  })



//EXTRAS------------------------------------------------------------------------------------------------------------------------------

// A layer with minResolution (hidden on hight zoom level)
var mapbox = new ol.layer.Tile({
  title: "Pirate Map",
  displayInLayerSwitcher: false,
  minResolution: 1223,
  source: new ol.source.XYZ({
    attributions: [
      '&copy; <a href="https://www.mapbox.com/map-feedback/">Mapbox</a> ',
      ol.source.OSM.ATTRIBUTION,
    ],
    url: "https://{a-d}.tiles.mapbox.com/v3/aj.Sketchy2/{z}/{x}/{y}.png",
  }),
});
// An overlay that stay on top
var labels = new ol.layer.Tile({
  title: "Labels (on top)",
  allwaysOnTop: true, // Stay on top of layer switcher
  noSwitcherDelete: true, // Prevent deleting from layer switcher
  source: new ol.source.Stamen({ layer: "terrain-labels" }),
});
// WMS with bbox
var brgm = new ol.layer.Tile({
  title: "GEOLOGIE",
  extent: [
    -653182.6969582437, 5037463.842847037, 1233297.5065495989,
    6646432.677299531,
  ],
  minResolution: 3.527777777777778,
  maxResolution: 3527.777777777778,
  source: new ol.source.TileWMS({
    url: "https://geoservices.brgm.fr/geologie",
    projection: "EPSG:3857",
    params: {
      LAYERS: "GEOLOGIE",
      FORMAT: "image/png",
      VERSION: "1.3.0",
    },
    attributions: ["<a href='http://www.brgm.fr/'>&copy; Brgm</a>"],
  }),
});
