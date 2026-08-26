#include <string.h>
void c_tn_005(const char *input) {
    char buf[12] = "id:";
    /* XG-BENCH:C-TN-005 START */
    size_t room = sizeof(buf) - strlen(buf) - 1;
    strncat(buf, input, room);
    /* XG-BENCH:C-TN-005 END */
}
