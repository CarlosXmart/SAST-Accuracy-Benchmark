using System.IO;
class CsTp002 {
  public static string Read(string name) {
    // XG-BENCH:CS-TP-002 START
    return File.ReadAllText(Path.Combine("/srv/data", name));
    // XG-BENCH:CS-TP-002 END
  }
}
