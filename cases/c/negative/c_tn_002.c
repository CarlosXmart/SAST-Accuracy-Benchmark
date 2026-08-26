#include <stdio.h>
void c_tn_002(const char *input) {
    char buf[16];
    /* XG-BENCH:C-TN-002 START */
    snprintf(buf, sizeof(buf), "name=%s", input);
    /* XG-BENCH:C-TN-002 END */
}
