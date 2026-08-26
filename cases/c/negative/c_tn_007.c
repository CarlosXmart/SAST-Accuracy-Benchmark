#include <stdlib.h>
#include <unistd.h>
int c_tn_007(char *tmpl) {
    /* XG-BENCH:C-TN-007 START */
    return mkstemp(tmpl);
    /* XG-BENCH:C-TN-007 END */
}
