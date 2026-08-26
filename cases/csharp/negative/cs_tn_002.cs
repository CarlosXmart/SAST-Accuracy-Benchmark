using System; using System.IO;
class CsTn002 {
  public static string Read(string name) {
    // XG-BENCH:CS-TN-002 START
    var baseDir = Path.GetFullPath("/srv/data") + Path.DirectorySeparatorChar;
    var target = Path.GetFullPath(Path.Combine(baseDir, name));
    if (!target.StartsWith(baseDir, StringComparison.Ordinal)) throw new UnauthorizedAccessException();
    return File.ReadAllText(target);
    // XG-BENCH:CS-TN-002 END
  }
}
