<?php
require 'notorm/NotORM.php';

$pdo = new \PDO('sqlite:test.db', null, null, [
    PDO::ERR_NONE => PDO::ERRMODE_EXCEPTION
]);
$db = new NotORM($pdo);

foreach ($db->pivo as $pivo) {
    echo "$pivo[znacka] $pivo[stupne]\n";
    echo "$pivo->stamgast[jmeno]}\n";
}