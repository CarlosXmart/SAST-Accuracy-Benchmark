#include <stdio.h>
void c_tn_001(const char *input) {
    char buf[8];
    /* XG-BENCH:C-TN-001 START */
    snprintf(buf, sizeof(buf), "%s", input);
    /* XG-BENCH:C-TN-001 END */
}
