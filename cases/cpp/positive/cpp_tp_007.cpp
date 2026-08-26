#include <fstream>
#include <string>
bool cpp_tp_007(const std::string &name) {
    // XG-BENCH:CPP-TP-007 START
    std::ifstream in("/srv/data/" + name);
    return in.good();
    // XG-BENCH:CPP-TP-007 END
}
