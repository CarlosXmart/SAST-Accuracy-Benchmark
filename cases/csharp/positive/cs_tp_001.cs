using System.Diagnostics;
class CsTp001 {
  public static void Run(string input) {
    // XG-BENCH:CS-TP-001 START
    Process.Start("cmd.exe", "/c echo " + input);
    // XG-BENCH:CS-TP-001 END
  }
}
