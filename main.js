let mapView = new ol.View({
    center: ol.proj.fromLonLat([97.20315611981032, 5.115938110484906]),
    zoom: 15,
});

let map = new ol.Map({
    target: "map",
    view: mapView,
});

let layerGroup = new ol.layer.Group({
    title: "Digitasi Layers",
    layers: [],
});

// Create popup Info layer
let container = document.getElementById('popup');
let content = document.getElementById('popup-content');
let closer = document.getElementById('popup-closer');

addController();
addLayer();

function addController() {
    let osmTile = new ol.layer.Tile({
        title: "Open Street Map",
        visible: true,
        source: new ol.source.OSM(),
    });
    map.addLayer(osmTile);

    let sidebar = new ol.control.Sidebar({
        element: "sidebar",
        position: "left",
    });
    map.addControl(sidebar);

    let layerSwitcher = new ol.control.LayerSwitcher({
        activitionMode: "click",
        startActive: false,
        groupSelectStyle: "children",
    });
    map.addControl(layerSwitcher);
}

function toggleLayer(e) {
    let layerName = e.target.value;
    let checkedStatus = e.target.checked;
    let layerList = map.getLayers();

    layerList.forEach(function (ele) {
        if (layerName == ele.get("title")) {
            ele.setVisible(checkedStatus);
        }
    });

    layerGroup.getLayers().forEach(function (ele) {
        ele.getLayers().forEach(function (ele2) {
            if (layerName == ele2.get("title")) {
                ele2.setVisible(checkedStatus);
            }
        });
    });
}

var hasil = null;
var dapat = false;

function getFeatureInfo(newLayer) {
    let popup = new ol.Overlay({
        element: container,
        autoPan: true,
        autoAnimation: {
            duration: 250
        }
    });

    map.addOverlay(popup);

    closer.onclick = function () {
        popup.setPosition(undefined);
        closer.blur();
    };

    map.on("singleclick", function (evt) {
        const viewResolution = /** @type {number} */ (
            mapView.getResolution()
        );
        
        const url = newLayer
            .getSource()
            .getFeatureInfoUrl(evt.coordinate, viewResolution, "EPSG:3857", {
                INFO_FORMAT: "text/html",
            });

        if (url) {
            fetch(url)
                .then((response) => response.text())
                .then((html) => {
                    if (!(html.toString().includes("<td>"))) {
                        dapat = false
                    } else {
                        dapat = true
                    }

                    if (dapat == true) {
                        hasil = html
                    }

                    if (hasil != null && (hasil.toString().includes("<td>"))) {
                        content.innerHTML = hasil;
                        popup.setPosition(evt.coordinate);
                    } else {
                        content.innerHTML = "Kosong";
                        popup.setPosition(evt.coordinate);
                    }
                    
                    map.un("singleclick");
                    map.un("pointermove");
                    return
                }).catch(() => {
                    return
                });
        }
        hasil = null
    });
}

function addCheckbox(layer, group) {
    // Tambahkan checkbox ke grup yang sesuai
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.value = layer.title;
    checkbox.checked = true;
    checkbox.onchange = function (event) {
        toggleLayer(event);
    };

    let label = document.createElement("label");
    label.htmlFor = layer.title;
    label.appendChild(document.createTextNode(layer.title));

    // Tentukan grup yang sesuai berdasarkan folder
    let nameGroup = group.folder
        .replace("Digitasi", "")
        .replace(/\s/g, "");
    let groupContainer = document.getElementById(
        nameGroup.toLowerCase() + "Group"
    );
    groupContainer.appendChild(checkbox);
    groupContainer.appendChild(label);
    groupContainer.appendChild(document.createElement("br"));
}

function addLayer() {
    map.addLayer(layerGroup);

    fetch("http://localhost/gis-sultan/read_shapefiles.php")
        .then((response) => response.json())
        .then((data) => {
            data.forEach((group) => {
                let groupLayer = new ol.layer.Group({
                    title: group.folder,
                    layers: [], // Menambahkan lapisan ke sini
                });

                group.layers.forEach((layer) => {
                    let newLayer = new ol.layer.Tile({
                        title: layer.title,
                        source: new ol.source.TileWMS({
                            url: "http://localhost:8080/geoserver/gampong/wms?",
                            params: { LAYERS: layer.layerName, TILED: false },
                            serverType: "geoserver",
                            visible: false,
                        }),
                    });

                    getFeatureInfo(newLayer)

                    groupLayer.getLayers().push(newLayer);

                    addCheckbox(layer, group)
                });

                layerGroup.getLayers().push(groupLayer); // Menambahkan grup ke grup utama
            });
        })
        .catch((error) => console.error("Error:", error));
}
