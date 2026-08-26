import java.nio.file.*;
class JavaTp003 {
  static String read(String name) throws Exception {
    // XG-BENCH:JAVA-TP-003 START
    Path p = Paths.get("/srv/data").resolve(name);
    return Files.readString(p);
    // XG-BENCH:JAVA-TP-003 END
  }
}
