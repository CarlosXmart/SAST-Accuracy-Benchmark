package cases
import ("fmt"; "net/http"; "net/url")
func GoTn006(raw string) (*http.Response,error) {
    // XG-BENCH:GO-TN-006 START
    u, err := url.Parse(raw); if err != nil { return nil, err }
    if u.Scheme != "https" || u.Hostname() != "api.example.test" { return nil, fmt.Errorf("blocked") }
    return http.Get(u.String())
    // XG-BENCH:GO-TN-006 END
}
