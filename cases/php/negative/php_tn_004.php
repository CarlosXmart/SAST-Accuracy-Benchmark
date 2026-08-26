<?php
function php_tn_004(string $payload) {
    // XG-BENCH:PHP-TN-004 START
    return json_decode($payload, true, 32, JSON_THROW_ON_ERROR);
    // XG-BENCH:PHP-TN-004 END
}
