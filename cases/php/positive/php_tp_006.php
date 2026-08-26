<?php
function php_tp_006($db, string $user) {
    // XG-BENCH:PHP-TP-006 START
    return $db->query("SELECT * FROM users WHERE name='" . $user . "'");
    // XG-BENCH:PHP-TP-006 END
}
