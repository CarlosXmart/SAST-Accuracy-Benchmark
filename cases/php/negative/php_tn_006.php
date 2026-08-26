<?php
function php_tn_006(PDO $db, string $user) {
    // XG-BENCH:PHP-TN-006 START
    $stmt = $db->prepare('SELECT * FROM users WHERE name = :name');
    $stmt->execute(['name' => $user]);
    return $stmt->fetchAll();
    // XG-BENCH:PHP-TN-006 END
}
