#include <cstdio>
void cpp_tn_001(const char *input) {
    char buf[8];
    // XG-BENCH:CPP-TN-001 START
    std::snprintf(buf, sizeof(buf), "%s", input);
    // XG-BENCH:CPP-TN-001 END
}
