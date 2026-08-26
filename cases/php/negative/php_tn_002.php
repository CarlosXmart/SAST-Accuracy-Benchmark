<?php
function php_tn_002(string $value): int {
    // XG-BENCH:PHP-TN-002 START
    return filter_var($value, FILTER_VALIDATE_INT, FILTER_NULL_ON_FAILURE) ?? 0;
    // XG-BENCH:PHP-TN-002 END
}
