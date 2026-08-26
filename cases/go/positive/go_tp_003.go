package cases
import "crypto/tls"
func GoTp003() *tls.Config {
    // XG-BENCH:GO-TP-003 START
    return &tls.Config{InsecureSkipVerify: true}
    // XG-BENCH:GO-TP-003 END
}
