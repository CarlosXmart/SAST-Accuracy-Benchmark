package cases
import ("os"; "path/filepath")
func GoTp002(name string) ([]byte,error) {
    // XG-BENCH:GO-TP-002 START
    return os.ReadFile(filepath.Join("/srv/data", name))
    // XG-BENCH:GO-TP-002 END
}
