using System.Diagnostics;
class CsTn001 {
  public static Process? Run(string input) {
    // XG-BENCH:CS-TN-001 START
    var psi = new ProcessStartInfo("dotnet") { UseShellExecute = false };
    psi.ArgumentList.Add("--info");
    return Process.Start(psi);
    // XG-BENCH:CS-TN-001 END
  }
}
