import java.nio.file.*;
class JavaTn003 {
  static String read(String name) throws Exception {
    // XG-BENCH:JAVA-TN-003 START
    Path base = Paths.get("/srv/data").toAbsolutePath().normalize();
    Path p = base.resolve(name).normalize();
    if (!p.startsWith(base)) throw new SecurityException("outside base");
    return Files.readString(p);
    // XG-BENCH:JAVA-TN-003 END
  }
}
