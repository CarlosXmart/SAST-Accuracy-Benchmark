package cases
import "crypto/rand"
func GoTn004(buf []byte) error {
    // XG-BENCH:GO-TN-004 START
    _, err := rand.Read(buf); return err
    // XG-BENCH:GO-TN-004 END
}
