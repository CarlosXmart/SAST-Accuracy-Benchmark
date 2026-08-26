package cases
import ("fmt"; "os"; "path/filepath"; "strings")
func GoTn002(name string) ([]byte,error) {
    // XG-BENCH:GO-TN-002 START
    base := filepath.Clean("/srv/data")
    target := filepath.Clean(filepath.Join(base, name))
    rel, err := filepath.Rel(base, target); if err != nil { return nil, err }
    if rel == ".." || strings.HasPrefix(rel, ".."+string(os.PathSeparator)) { return nil, fmt.Errorf("outside base") }
    return os.ReadFile(target)
    // XG-BENCH:GO-TN-002 END
}
