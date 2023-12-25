var mapView = new ol.View ({
    center: ol.proj.fromLonLat([97.20315611981032, 5.115938110484906]),
    zoom: 15,
})

var map = new ol.Map ({
    target: 'map',
    view: mapView,
})

var layerGroup = new ol.layer.Group({
    title: 'Digitasi Layers',
    layers: [],
});


addController()
addLayer()


function addController() {
    var osmTile = new ol.layer.Tile({
        title: 'Open Street Map',
        visible: true,
        source: new ol.source.OSM()
    })
    map.addLayer(osmTile)
    
    var sidebar = new ol.control.Sidebar({ element: 'sidebar', position: 'left' });
    map.addControl(sidebar);
    
    var layerSwitcher = new ol.control.LayerSwitcher({
        activitionMode: 'click',
        startActive: false,
        groupSelectStyle: 'children'
    })
    map.addControl(layerSwitcher)
}

function toggleLayer(e) {
    var layerName = e.target.value;
    var checkedStatus = e.target.checked;
    var layerList = map.getLayers()

    layerList.forEach(function(ele){
        if (layerName == ele.get('title')) {
            ele.setVisible(checkedStatus)
        }
    })

    layerGroup.getLayers().forEach(function(ele){
        ele.getLayers().forEach(function(ele2){
            if (layerName == ele2.get('title')) {
                ele2.setVisible(checkedStatus)
            }
        })
    })
}


function addLayer() {
    map.addLayer(layerGroup);
    
    fetch('http://localhost/gis-sultan/read_shapefiles.php')
        .then(response => response.json())
        .then(data => {
            data.forEach(group => {
                var groupLayer = new ol.layer.Group({
                    title: group.folder,
                    layers: [], // Menambahkan lapisan ke sini
                });
    
                group.layers.forEach(layer => {
                    var newLayer = new ol.layer.Tile({
                        title: layer.title,
                        source: new ol.source.TileWMS({
                            url: 'http://localhost:8080/geoserver/gampong/wms?',
                            params: {'LAYERS': layer.layerName, 'TILED': false},
                            serverType: 'geoserver',
                            visible: false,
                        }),
                    });
    
                    groupLayer.getLayers().push(newLayer);

                    // Tambahkan checkbox ke grup yang sesuai
                    var checkbox = document.createElement('input');
                    checkbox.type = 'checkbox';
                    checkbox.value = layer.title;
                    checkbox.checked = true;
                    checkbox.onchange = function (event) {
                        toggleLayer(event);
                    };

                    var label = document.createElement('label');
                    label.htmlFor = layer.title;
                    label.appendChild(document.createTextNode(layer.title));

                    let nameGroup = group.folder.replace("Digitasi", "").replace(/\s/g, '')
                    var groupContainer = document.getElementById(nameGroup.toLowerCase() + 'Group');
                    groupContainer.appendChild(checkbox);
                    groupContainer.appendChild(label);
                    groupContainer.appendChild(document.createElement('br'));
                });
    
                layerGroup.getLayers().push(groupLayer);
            });
        })
        .catch(error => console.error('Error:', error));
}