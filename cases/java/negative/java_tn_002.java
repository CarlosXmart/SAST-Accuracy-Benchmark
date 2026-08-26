import java.util.*;
class JavaTn002 {
  static Process run(String user) throws Exception {
    // XG-BENCH:JAVA-TN-002 START
    return new ProcessBuilder(List.of("printf", "%s", user)).start();
    // XG-BENCH:JAVA-TN-002 END
  }
}
