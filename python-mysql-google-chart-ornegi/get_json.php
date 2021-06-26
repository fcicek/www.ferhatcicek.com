<?php

$con = mysql_connect('localhost', 'raspberry', 'pi') or die('veri tabani baglanti hatasi');
mysql_select_db('raspberry_system', $con); 
$query = mysql_query('SELECT * FROM cpu_temp');

$table = array();
$table['cols'] = array(
    array('label' => 'saat', 'type' => 'string'),
	array('label' => 'sicaklik', 'type' => 'number')
);

$rows = array();
while($r = mysql_fetch_assoc($query)) {
    $tempa = array();
	$tempa[] = array('v' => $r['saat']);
	$tempa[] = array('v' => (int) $r['sicaklik']); 
    $rows[] = array('c' => $tempa);
}

$table['rows'] = $rows;

$jsonTable = json_encode($table);

header('Cache-Control: no-cache, must-revalidate');
header('Expires: Mon, 26 Jul 1997 05:00:00 GMT');
header('Content-type: application/json');

echo $jsonTable;
?>
