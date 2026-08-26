import java.net.*; import java.io.*;
class JavaTp006 {
  static InputStream fetch(String url) throws Exception {
    // XG-BENCH:JAVA-TP-006 START
    return new URL(url).openStream();
    // XG-BENCH:JAVA-TP-006 END
  }
}
