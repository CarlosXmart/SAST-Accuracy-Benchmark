package cases
import "crypto/sha256"
func GoTn005(data []byte) [32]byte {
    // XG-BENCH:GO-TN-005 START
    return sha256.Sum256(data)
    // XG-BENCH:GO-TN-005 END
}
