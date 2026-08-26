#include <cstring>
void cpp_tp_005(const char *input) {
    char *buf = new char[8];
    // XG-BENCH:CPP-TP-005 START
    std::strcpy(buf, input);
    // XG-BENCH:CPP-TP-005 END
    delete[] buf;
}
