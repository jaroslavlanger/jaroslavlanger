<?php

$db = new \PDO('sqlite:test.db', null, null, [
    PDO::ERR_NONE => PDO::ERRMODE_EXCEPTION
]);
$db->query('DROP TABLE stamgast');
$db->query('
CREATE TABLE stamgast (
id INTEGER PRIMARY KEY,
jmeno VARCHAR(30)
);');

$db->query('DROP TABLE pivo');
$db->query('
CREATE TABLE pivo (
    id INTEGER PRIMARY KEY,
    znacka VARCHAR(30),
    stupne INTEGER,
    vypil INTEGER,
    FOREIGN KEY (vypil) REFERENCES stamgast(id)
);');

$data = [
    'alois',
    'bedrich',
    'cyril',
    'david',
    'eduard' 
];

$statement = $db->prepare('INSERT INTO stamgast(jmeno) VALUES (:jmeno)');

$ids = [];
foreach ($data as $name) {
    $statement->execute(['jmeno' => $name]);
    $ids[$name] = $db->lastInsertId();
}

$data = [
    ['plzen', 12, $ids['alois'] ],
    ['starobrno', 11, $ids['bedrich'] ],
    ['svijany', 13, $ids['cyril'] ],
    ['staropramen', 10, $ids['eduard'] ]
];

$statement = $db->prepare('INSERT INTO pivo(znacka, stupne, vypil) VALUES (:znacka,:stupne,:vypil)');
foreach ($data as $item) {
    $statement->execute([
        'znacka' => $item[0],
        'stupne' => $item[1],
        'vypil' => $item[2],
        ]);
}

//$statement = $db->prepare('SELECT * FROM stamgast LEFT JOIN pivo ON pivo.vypil=stamgast.id');
$statement = $db->prepare('SELECT * FROM stamgast');

$statement->execute();

$fetched = $statement->fetchAll(PDO::FETCH_ASSOC);
//->fetch(PDO::FETCH_ASSOC);
print_r($fetched);
    
/*/
do {
    $fet = $statement->fetch();    
    print_r($fet);
} while ($fet);
/*/