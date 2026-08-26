#include <fstream>
#include <string>
bool cpp_tn_007(const std::string &name) {
    // XG-BENCH:CPP-TN-007 START
    if (name.find('/') != std::string::npos || name.find('\\') != std::string::npos || name.find("..") != std::string::npos) return false;
    std::ifstream in("/srv/data/" + name);
    return in.good();
    // XG-BENCH:CPP-TN-007 END
}
