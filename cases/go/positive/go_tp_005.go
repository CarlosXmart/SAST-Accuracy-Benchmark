package cases
import "crypto/md5"
func GoTp005(data []byte) [16]byte {
    // XG-BENCH:GO-TP-005 START
    return md5.Sum(data)
    // XG-BENCH:GO-TP-005 END
}
