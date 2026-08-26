package cases
import "net/http"
func GoTp006(raw string) (*http.Response,error) {
    // XG-BENCH:GO-TP-006 START
    return http.Get(raw)
    // XG-BENCH:GO-TP-006 END
}
