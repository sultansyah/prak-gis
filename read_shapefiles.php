<?php
$folderPaths = [
    'Digitasi Point',
    'Digitasi Polygon',
    'Digitasi Polyline',
];

$data = [];

foreach ($folderPaths as $folderPath) {
    $files = glob($folderPath . '/*.shp');

    $group = [
        'folder' => basename($folderPath),
        'layers' => [],
    ];

    foreach ($files as $file) {
        $filename = pathinfo($file, PATHINFO_FILENAME);
        $lowercaseFilename = strtolower($filename);

        $group['layers'][] = [
            'title' => $filename,
            'layerName' => 'gampong:' . $lowercaseFilename,
        ];
    }

    $data[] = $group;
}

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header('Content-Type: application/json');
echo json_encode($data);
?>
