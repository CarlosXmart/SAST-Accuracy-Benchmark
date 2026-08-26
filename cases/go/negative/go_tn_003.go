package cases
import "crypto/tls"
func GoTn003() *tls.Config {
    // XG-BENCH:GO-TN-003 START
    return &tls.Config{MinVersion: tls.VersionTLS12}
    // XG-BENCH:GO-TN-003 END
}
