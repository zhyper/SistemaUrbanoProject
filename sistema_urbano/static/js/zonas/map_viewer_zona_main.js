//custom control

// class RotateNorthControl extends ol.control.Control {
//   /**
//    * @param {Object} [opt_options] Control options.
//    */
//   constructor(opt_options) {
//     const options = opt_options || {};

//     const button = document.createElement("button");
//     button.innerHTML = "N";

//     const element = document.createElement("div");
//     element.className = "rotate-north ol-unselectable ol-control btn-north";
//     element.appendChild(button);

//     super({
//       element: element,
//       target: options.target,
//     });

//     button.addEventListener("click", this.handleRotateNorth.bind(this), false);
//   }
//   handleRotateNorth() {
//     this.getMap().getView().setRotation(0);
//   }
// }

// class ToppanelControl extends ol.control.Control {
//   constructor(opt_options) {
//     const options = opt_options || {};
//     const element = document.getElementById("top-menu");

//     super({
//       element: element,
//       target: options.target,
//     });
//   }
// }

function toUpperCase(str) {
  return str.toUpperCase();
}

//DATA from DJANGO----------------------------------------------------
//const zonas = JSON.parse(data);

/*
zonas.forEach((item) => {
  console.log(item.fields.codigo_zona);
});
*/

//END DATA from DJANGO-----------------------------------------------

var viewPopup = false;

var view = new ol.View({
  center: ol.proj.fromLonLat([-71.9774868, -13.5169427]),
  zoom: 13,
  // rotation: 1,
});

const zip = new JSZip();

function getKMLData(buffer) {
  let kmlData;
  zip.load(buffer);
  const kmlFile = zip.file(/.kml$/i)[0];
  if (kmlFile) {
    kmlData = kmlFile.asText();
  }
  return kmlData;
}

function getKMLImage(href) {
  let url = href;
  let path = window.location.href;
  path = path.slice(0, path.lastIndexOf("/") + 1);
  if (href.indexOf(path) === 0) {
    const regexp = new RegExp(href.replace(path, "") + "$", "i");
    const kmlFile = zip.file(regexp)[0];
    if (kmlFile) {
      url = URL.createObjectURL(new Blob([kmlFile.asArrayBuffer()]));
    }
  }
  return url;
}

// Define a KMZ format class by subclassing ol/format/KML

class KMZ extends ol.format.KML {
  constructor(opt_options) {
    const options = opt_options || {};
    options.iconUrlFunction = getKMLImage;
    super(options);
  }

  getType() {
    return "arraybuffer";
  }

  readFeature(source, options) {
    const kmlData = getKMLData(source);
    return super.readFeature(kmlData, options);
  }

  readFeatures(source, options) {
    const kmlData = getKMLData(source);
    return super.readFeatures(kmlData, options);
  }
}

// Set up map with Drag and Drop interaction

const dragAndDropInteraction = new ol.interaction.DragAndDrop({
  formatConstructors: [
    KMZ,
    ol.format.GPX,
    ol.format.GeoJSON,
    ol.format.IGC,
    ol.format.KML,
    ol.format.TopoJSON,
  ],
});

dragAndDropInteraction.on("addfeatures", function (event) {
  const vectorSource = new ol.source.Vector({
    features: event.features,
  });
  map.addLayer(
    new ol.layer.Vector({
      source: vectorSource,
    })
  );
  map.getView().fit(vectorSource.getExtent());
});

// The Map
/*
var map = new ol.Map({
  target: "map",
  view: new ol.View({
    zoom: 11,
    center: [260497, 6249720],
  }),
  layers: [baseLayers, mapbox, brgm, baseLayersZhyper, labels],
});
*/

//-----OverView MAP---------------------------------------------------

const overviewMapControl = new ol.control.OverviewMap({
  // see in overviewmap-custom.html to see the custom CSS used
  className: 'ol-overviewmap ol-custom-overviewmap',
  layers: [
    /*new ol.layer.Tile({
      source: new ol.source.OSM(),

    }),*/
    new ol.layer.Tile({
      title: "Google Map Roadmap",
      baseLayer: true,
      visible: true,
      // Again set this layer as a base layer
      //visible: true,
      source: new ol.source.XYZ({
        // HYBRID
        //url: "http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}", 
        // ROADMAP
        url: "http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}",
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
          'FORMAT_OPTIONS': 'antialias:text',
          //'cql_filter': "codigo_zre ='" + codigo_zona+ "'"
        },
        serverType: 'geoserver',
        // Countries have transparency, so do not fade tiles:
        //transition: 0,
      }),
    }),
  ],
  collapseLabel: '\u00BB',
  label: '\u00AB',
  collapsed: true,
});


//---------------------------------------------------------------
const popup = new ol.Overlay({
  element: container,
  autoPan: true,
  autoPanAnimation: {
    duration: 250,
  },
});

closer.onclick = function () {
  console.log("closer");
  popup.setPosition(undefined);
  closer.blur();
  return false;
};

const map = new ol.Map({
  //controls: ol.control.defaults().extend([new RotateNorthControl()]),
  //controls: ol.interaction.defaults().extend([overviewMapControl]),
  interactions: ol.interaction.defaults({dragPan: false, mouseWheelZoom: false}).extend([
      dragAndDropInteraction,
  
      new ol.interaction.DragPan({
            condition: function (event) {
              return this.getPointerCount() === 2 || ol.events.condition.platformModifierKeyOnly(event);
            },
          }),
      new ol.interaction.MouseWheelZoom({
            condition: ol.events.condition.platformModifierKeyOnly,
          }),
        ]),
  layers: [
    /*  
  new ol.layer.Tile({
      source: new ol.source.OSM(),
    }),
    new ol.layer.Image({
      //title: 'Inmebles Relig. Bloques 1er Nivel',
      visible: true,
      source: new ol.source.ImageWMS({
        url: "http://localhost:8080/geoserver/sgotp-41zre/wms",
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
    */

    baseLayers,
    baseLayerPDU2013,
    baseLayer41ZRECarac,
    baseLayer41ZREProp,
    baseLayer41ZREBase,
    //mapbox,
    //brgm,
    //labels,
  ],
  target: "map_viewer_zona_main",
  view: view,
  overlays: [popup],
});

//var sidebar = new ol.control.Sidebar({ element: 'sidebar', position: 'left' });

//map.addControl(sidebar);

map.addControl(overviewMapControl);

// Add control inside the map
var ctrl = new ol.control.LayerSwitcher({
  // collapsed: false,
  // mouseover: true
});
map.addControl(ctrl);
ctrl.on("toggle", function (e) {
  console.log("Collapse layerswitcher", e.collapsed);
});

// Add a layer switcher outside the map
var switcher = new ol.control.LayerSwitcher({
  target: $(".layerSwitcher").get(0),
  // displayInLayerSwitcher: function (l) { return false; },
  show_progress: true,
  extent: true,
  trash: true,
  oninfo: function (l) {
    alert(l.get("title"));
  },
});
// Add a new button to the list
switcher.on("drawlist", function (e) {
  var layer = e.layer;
  $("<div>")
    .text("?") // addClass('layerInfo')
    .click(function () {
      alert(layer.get("title"));
    })
    .appendTo($("> .ol-layerswitcher-buttons", e.li));
});
// Add a button to show/hide the layers
var button = $('<div class="toggleVisibility" title="show/hide">')
  .text("Show/hide all")
  .click(function () {
    var a = map.getLayers().getArray();
    var b = !a[0].getVisible();
    if (b) button.removeClass("show");
    else button.addClass("show");
    for (var i = 0; i < a.length; i++) {
      a[i].setVisible(b);
    }
  });
switcher.setHeader($("<div>").append(button).get(0));

map.addControl(switcher);
// Insert mapbox layer in layer switcher
function displayInLayerSwitcher(b) {
  mapbox.set("displayInLayerSwitcher", b);
}

// Get options values
if ($("#opb").prop("checked")) $("body").addClass("hideOpacity");
if ($("#percent").prop("checked")) $("body").addClass("showPercent");
if ($("#dils").prop("checked")) displayInLayerSwitcher(true);
/******/

//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

const displayFeatureInfo = function (pixel) {
  const features = [];
  map.forEachFeatureAtPixel(pixel, function (feature) {
    features.push(feature);
  });
  if (features.length > 0) {
    const info = [];
    let i, ii;
    for (i = 0, ii = features.length; i < ii; ++i) {
      const description =
        features[i].get("description") ||
        features[i].get("name") ||
        features[i].get("_name") ||
        features[i].get("layer");
      if (description) {
        info.push(description);
      }
    }
    document.getElementById("info").innerHTML = info.join("<br/>") || "&nbsp";
  } else {
    document.getElementById("info").innerHTML = "&nbsp;";
  }
};

map.on("pointermove", function (evt) {
  if (evt.dragging) {
    return;
  }
  const pixel = map.getEventPixel(evt.originalEvent);
  displayFeatureInfo(pixel);

  /*
    const data = wmsLayer.getData(evt.pixel);
    const hit = data && data[3] > 0; // transparent pixels have zero for data[3]
    map.getTargetElement().style.cursor = hit ? 'pointer' : '';

    */
});

/*
  map.on("click", function (evt) {
    displayFeatureInfo(evt.pixel);
  });
  */

// Sample data download

const link = document.getElementById("download");

function download(fullpath, filename) {
  fetch(fullpath)
    .then(function (response) {
      return response.blob();
    })
    .then(function (blob) {
      if (navigator.msSaveBlob) {
        // link download attribute does not work on MS browsers
        navigator.msSaveBlob(blob, filename);
      } else {
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        link.click();
      }
    });
}
/*
document.getElementById("download-kmz").addEventListener("click", function () {
  download("data/kmz/iceland.kmz", "iceland.kmz");
});
*/

map.on("click", (evt) => {
  //limpiado el arreglo de Informacion
  var infoGeneral0 = [];
  infoGeneralText = "";
  popupText = "";
  coord0 = "";
  //infoGeneral.length = 0;

  const viewResolution = view.getResolution();

  // @type {number}

  WMSSources.map((wms) => {
    if (wms) {
      var url = wms.getFeatureInfoUrl(
        evt.coordinate,
        viewResolution,
        "EPSG:3857",

        { INFO_FORMAT: "application/json" }
      );

      if (url) {
        fetch(url)
          .then((response) => {
            //para que obtengamos un JSON en vez de un HTML
            return response.json();
            //    console.log(response.text());
          })
          .then((html) => {
            //document.getElementById('info2').innerHTML = html;
            //convirtiendo a objeto JSON
            var data = html;
            console.log("info_data: ", data.features);

            //-------------------
            var coordinate = evt.coordinate;
            var hdms = ol.coordinate.toStringXY(
              ol.proj.toLonLat(coordinate),
              6
            );
            //var foto = info_zona.features[0].properties.codregistr;

            if (data.features[0]) {
              //element.innerHTML = `<p>${data.features[0].id}</p>`;

              infoGeneral0.push({
                layer: data.features[0].id,
                properties: data.features[0].properties,
                coordinate: hdms,
              });
              viewPopup = true;
              // console.log("element:", infoGeneral0[0].layer);
            }

            // console.log("coordinate: " + hdms);
            popup.setPosition(coordinate);
          });
        // .then(()=>{
        //   console.log('3er then: ',infoGeneral0)
        // } )
      }
      //content.innerHTML = infoGeneral[0].layer;
    }
  });

  console.log("INFO GENERAL", infoGeneral0);

  //-----------------------------
  function renderPopup(datas){

    $.map(infoGeneral0, function( info, i){
      console.log("Infogeneral map: ",info)
      popupText = popupText + info
    })

  }

  //renderPopup()
  //-----------------------------

  function getDataInfo() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(infoGeneral0);
      }, 1000);
    });
  }

  async function showInfoZre(data) {
    console.log("info zre AJAX");

    const linea = `<p>
    ${data.nombre}
    </p>`;
    return linea;
    // console.log('info zre AJAX');
  }

  function doTheThing(codigo) {
    return new Promise((resolve, reject) => {
      $.ajax({
        //url: `http://144.91.84.249:3011/api/planes/zona/${codigo}`,
        url: `http://144.91.84.249/api/planesfull/codigozona/${codigo}`,
        type: "GET",
        dataType:'json',
        success: function (data) {
          resolve(data);
          console.log("Zona:", data);
          console.log("Nombre:", showInfoZre(data));
          popupText = popupText + data.nombre;
        },
        error: function (error) {
          reject(error);
        },
      });
    });
  }

  //Gestionando la Informacion contenida en el POPUP ---------------------------------------------------------------------------
  getDataInfo().then((res) => {

    res.map((dat) => {
      console.log("famoso dat: ", dat);

      //Identificando la Zonificacion del PDU 2013
      if (dat.layer.includes("pdu_2013_zonificacion")) {

        console.log("Zona: ", dat.properties.zona);
        
        $.ajax({
          url: `http://144.91.84.249/api/parametrospdu/${dat.properties.zona}`,
          type: "GET",
          dataType:'json',
          success: function (dataparam) {
            

            console.log("DATA PARAM", dataparam);
            
            $("#popup-content").append(
               `
                <div class="accordion accordion-flush" id="accordionInfoParamPDU">
    
                  <div class="accordion-item">
                    <h2 class="accordion-header" id="flush-headingOneInfoParamPDU">
                      <button class="accordion-button collapsed shadow-none fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOneInfoParamPDU" aria-expanded="false" aria-controls="flush-collapseOneInfoParamPDU">
                      <i class="ri-eye-line"></i> &nbsp; <i class="ri-table-line"></i>  &nbsp; Ver Parámetro PDU 2013
                      </button>
                    </h2>
                    <div id="flush-collapseOneInfoParamPDU" class="accordion-collapse collapse" aria-labelledby="flush-headingOneInfoParamPDU" data-bs-parent="#accordionInfoParamPDU">
                      <div class="accordion-body">
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Código Zonificación</strong></span><span>${dataparam.cod_zona}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Zonificación</strong></span><span>${dataparam.altura_edifica}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Tipo Zona</strong></span><span>${dataparam.tipo_zona}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Tipo Area</strong></span><span>${dataparam.tipo_area}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Usos</strong></span><span>${dataparam.usos}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Altura Edificatoria</strong></span><span>${dataparam.altura_edifica}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Coef. Edificatorio</strong></span><span>${dataparam.coeficiente_edifica}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Area Edificacion</strong></span><span>${dataparam.area_edifica}&nbsp;m.&sup2;</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Area Libre</strong></span><span>${dataparam.area_libre}&nbsp;m.&sup2;</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Estacionamiento</strong></span><span>${dataparam.estacionamiento}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Densidad Neta</strong></span><span>${dataparam.densidad_neta}</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Frente Mínimo</strong></span><span>${dataparam.frente_minimo}&nbsp;m.</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Lote Frente Mínimo</strong></span><span>${dataparam.lote_frente_minimo}&nbsp;m.</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Lote Mínimo</strong></span><span>${dataparam.lote_minimo}&nbsp;m.&sup2;</span></div></li>
                      <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Nivel de Servicio</strong></span><span>${dataparam.nivel_servicio}</span></div></li>

                      </div>
                    </div>
                  </div>
                </div>
              `);
          },
          error: function (error) {
            // reject(error)
          },
        });
      }

      //Identficando la Capa: MANZANAS -----------------------------------------------------------------------------------------
      if (dat.layer.includes("manzanas")) {

        popupText =
          popupText +
          `
          <ul class="list-group">
            <li class="list-group-item mt-1"><div class="item-list-mapa-popup"><span><strong>Manzana</strong></span><span>${dat.properties.manzana}</span></div></li>
          </ul>
          `;

      } 

      //Identficando la Capa: HABILITACIONES URBANAS --------------------------------------------------------------------------
      if (dat.layer.includes("habilitaciones")) {

        popupText =
          popupText +
          `
          <ul class="list-group">
            <li class="list-group-item mt-1"><div class="item-list-mapa-popup"><span><strong>Agrupaci&oacute;n Urbana</strong></span><span>${dat.properties.tipo}&nbsp;${dat.properties.nombre}</span></div></li>
          </ul>
          `;
      } 

      //Identficando la Capa: LOTES -----------------------------------------------------------------------------------------
      if (dat.layer.includes("lotes")) {
        //Asignado los datos del Lote a una variable: lote
        let lote = dat.properties;

        popupText =
          popupText +
          `
            <div class="accordion accordion-flush" id="accordionInfoLote">

            <div class="accordion-item">
              <h2 class="accordion-header" id="flush-headingOneInfoLote">
                <button class="accordion-button collapsed shadow-none fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOneInfoLote" aria-expanded="false" aria-controls="flush-collapseOneInfoLote">
                <i class="ri-eye-line"></i> &nbsp; <i class="ri-table-line"></i>  &nbsp; Ver detalle del Lote
                </button>
              </h2>
              <div id="flush-collapseOneInfoLote" class="accordion-collapse collapse" aria-labelledby="flush-headingOneInfoLote" data-bs-parent="#accordionInfoLote">
                <div class="accordion-body">
                <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Codigo</strong></span><span>${lote.ccodficha}</span></div></li>
                <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Titular [Nombre]</strong></span><span>${lote.cnombtitu}</span></div></li>
                <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Servicio Agua</strong></span><span>${lote.caguadetal}</span></div></li>
                <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Servicio Desague</strong></span><span>${lote.cdesague}</span></div></li>
                <li class="list-group-item"><div class="item-list-mapa-popup"><span><strong>Servicio Limpieza Pub.</strong></span><span>${lote.cservicelp}</span></div></li>
                </div>
              </div>
            </div>
            </div
          `;
      }

      //Identficando la Capa: ZONAS -----------------------------------------------------------------------------------------
      if (dat.layer.includes("zonas")) {
        doTheThing(dat.properties.codigo_zre);
        console.log("Zona-----veamos:", dat.properties.codigo_zre);
        //let url = "\{% include 'includes/lista.html' %\}"

        const oo = $.ajax({
          //url: `http://144.91.84.249:3011/api/planes/zona/${dat.properties.codigo_zre}`,
          url: `http://144.91.84.249/api/planesfull/codigozona/${dat.properties.codigo_zre}`,
          type: "GET",
          dataType:'json',
          beforeSend: function () {
            
            $(".loader").addClass("loader-active");
          },
          complete: function () {
            $(".loader").removeClass("loader-active");
          },

          success: function (data) {
            // resolve(data)
            console.log("Zonax:", data);

            $("#data-receiver").empty();
            $("#data-receiver").append(
              `<li>
                ${data[0].nombre}
              </li>
              `
            );
            $("#popup-content-header").empty();
            $("#popup-content-header").append(`
              <div class="alert alert-warning fw-bold p-1 m-0" role="alert">
                ${data[0].nombre}
              </div>
              
            `);
            
            //$("#popup-content").append(renderMapas(data.mapas));

            $("#popup-content").append(`
            
              <ul class="nav nav-tabs" id="myTabMapas" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link fw-bold active" id="caracterizacion-tab" data-bs-toggle="tab" data-bs-target="#caracterizacion" type="button" role="tab" aria-controls="caracterizacion" aria-selected="true"><i class="ri-search-line"></i>&nbsp;Caracterización</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link fw-bold" id="propuesta-tab" data-bs-toggle="tab" data-bs-target="#propuesta" type="button" role="tab" aria-controls="propuesta" aria-selected="false"><i class="ri-search-line"></i>&nbsp;Propuesta</button>
                </li>
                
              </ul>

              <div class="tab-content">
                <div class="tab-pane active" id="caracterizacion" role="tabpanel" aria-labelledby="caracterizacion-tab" tabindex="0">
                
                ${renderAccordion(data[0].mapas,1,data[0].zona.codigo_zona)}</div>
                <div class="tab-pane" id="propuesta" role="tabpanel" aria-labelledby="propuesta-tab" tabindex="0">
                
                ${renderAccordion(data[0].mapas,2,data[0].zona.codigo_zona)}</div>
              </div>



              
            `);

            return data.nombre;
          },
          error: function (error) {
            // reject(error)
          },
        });

        //console.log(oo);

        //listando el Codigo de la ZRE
        /*
        popupText =
          popupText +
          `
            <p>${dat.layer}</p>
            <ul>
              <li>${dat.properties.codigo_zre}</li>
            </ul>
          `;
        */
      }

      coord0 = dat.coordinate;
    });

    //Agregando la información de la Coordenada Generada
    //content.innerHTML = popupText + `<p>${coord0}</p>`;
    content.innerHTML = popupText;
    $("#popup-content-coordenada").empty();
    $("#popup-content-coordenada").append(`
    <li class="list-group-item border-0"><div class="item-list-mapa-popup item-right"><span class="mini"> Coordenas: ${coord0}</span></div></li>
    `);
  });


  //console.log("INFO GENERAL ending......", infoGeneral0);
});





function renderMapas( infex ){
  let lineas = ''
  infex.forEach((mapa)=>{
    lineas += ` 
        <li class="list-group-item">${mapa.nombre}</li>
      `
  })
  return ` <ul class="list-group">${lineas}</ul>`
}

function renderMapasByEtapa( mapas, etapa_plan){
  let lineas = ''
  mapas.forEach(mapa=>{
    if (mapa.plan_etapa_id == etapa_plan){
      lineas += ` 
      <li class="list-group-item">${mapa.nombre}</li>
    `
    } 
  })
  
  return ` <ul class="list-group scroll-map-list">${lineas}</ul>`

}




function renderAccordion( mapas, etapa_plan, codigo_zona ){

  function listarMapas( mapas, etapa_plan, componente, codigo_zona ){
    let lineas = ''
    //if (etapa_plan == 1){
      mapas.forEach(mapa=>{

        if (mapa.plan_etapa.id == etapa_plan){
          if (mapa.componente.nombre == componente){
              lineas += ` 
              <li class="list-group-item">
                <div class="item-list-mapa-popup">
                  <span>
                    <i class="ri-road-map-line"></i> &nbsp; <a href="${urlWebserver}:90/zre41media/images/mapas/${codigo_zona}/${toUpperCase(mapa.plan_etapa.slug)}/${mapa.componente.abreviacion}/${mapa.url}.jpg" data-lightbox="image-1" data-title="Nombre: ${mapa.nombre}">
                    <img src="${urlWebserver}:90/zre41media/images/mapas/${codigo_zona}/${toUpperCase(mapa.plan_etapa.slug)}/${mapa.componente.abreviacion}/thumbnails/${mapa.url}.jpg" class="card-img-top img-list-mapa-thumbnails" alt="..." title="pre visualizar">
                    </a>&nbsp; ${mapa.nombre}
                  </span>
                  <span>
                    <a href="${urlWebserver}:90/zre41media/images/mapas/${codigo_zona}/${toUpperCase(mapa.plan_etapa.slug)}/${mapa.componente.abreviacion}/${mapa.url}.pdf" data-bs-toggle="tooltip" data-bs-html="true" title="descargar" target='_blank' ><i class="ri-download-cloud-2-line"></i></a>
                  </span>
                </div>
              </li>
              `
          }
        }
      })
    //}
    return `<ul class="list-group scroll-map-list">${lineas}</ul>`
  }


  let linea = `
  <div class="accordion accordion-flush" id="accordion${etapa_plan}">

    <div class="accordion-item">
      <h2 class="accordion-header" id="flush-headingOne${etapa_plan}">
        <button class="accordion-button collapsed shadow-none fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne${etapa_plan}" aria-expanded="false" aria-controls="flush-collapseOne${etapa_plan}">
        <i class="ri-sun-foggy-line"></i> &nbsp; Ambiental
        </button>
      </h2>
      <div id="flush-collapseOne${etapa_plan}" class="accordion-collapse collapse" aria-labelledby="flush-headingOne${etapa_plan}" data-bs-parent="#accordion${etapa_plan}">
        <div class="accordion-body">
          ${listarMapas(mapas, etapa_plan, "Ambiental", codigo_zona)}
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <h2 class="accordion-header" id="flush-headingTwo${etapa_plan}">
        <button class="accordion-button collapsed shadow-none fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo${etapa_plan}" aria-expanded="false" aria-controls="flush-collapseTwo${etapa_plan}">
        <i class="ri-community-line"></i> &nbsp; Fisico Construido
        </button>
      </h2>
      <div id="flush-collapseTwo${etapa_plan}" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo${etapa_plan}" data-bs-parent="#accordion${etapa_plan}">
        <div class="accordion-body">
          ${listarMapas(mapas, etapa_plan, "Físico Construido", codigo_zona)}
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <h2 class="accordion-header" id="flush-headingThree${etapa_plan}">
        <button class="accordion-button collapsed shadow-none fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree${etapa_plan}" aria-expanded="false" aria-controls="flush-collapseThree${etapa_plan}">
        <i class="ri-earthquake-line"></i> &nbsp; Gestion de Riesgos de Desastres
        </button>
      </h2>
      <div id="flush-collapseThree${etapa_plan}" class="accordion-collapse collapse" aria-labelledby="flush-headingThree${etapa_plan}" data-bs-parent="#accordion${etapa_plan}">
        <div class="accordion-body">
          ${listarMapas(mapas, etapa_plan, "Gestión de Riesgos", codigo_zona)}
        </div>
      </div>
    </div>
    
  </div>
  `



  return ` ${linea}`
}






