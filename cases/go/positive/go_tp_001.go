package cases
import "os/exec"
func GoTp001(input string) *exec.Cmd {
    // XG-BENCH:GO-TP-001 START
    return exec.Command("sh", "-c", "echo "+input)
    // XG-BENCH:GO-TP-001 END
}
