<?php
function php_tn_005(string $data): string {
    // XG-BENCH:PHP-TN-005 START
    return hash('sha256', $data);
    // XG-BENCH:PHP-TN-005 END
}
