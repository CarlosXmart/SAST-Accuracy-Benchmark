package cases
import "os/exec"
func GoTn001(input string) *exec.Cmd {
    // XG-BENCH:GO-TN-001 START
    return exec.Command("printf", "%s", input)
    // XG-BENCH:GO-TN-001 END
}
