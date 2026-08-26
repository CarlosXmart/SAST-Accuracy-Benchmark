<?php
function php_tn_003(string $name) {
    // XG-BENCH:PHP-TN-003 START
    if ($name !== basename($name) || $name === '.' || $name === '..') { throw new Exception('invalid'); }
    return file_get_contents('/srv/data/' . $name);
    // XG-BENCH:PHP-TN-003 END
}
