<?php
function php_tp_003(string $name) {
    // XG-BENCH:PHP-TP-003 START
    return file_get_contents('/srv/data/' . $name);
    // XG-BENCH:PHP-TP-003 END
}
