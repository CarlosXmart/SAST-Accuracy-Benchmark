import java.net.*;
class JavaTp009 {
  static URLConnection send(String token) throws Exception {
    // XG-BENCH:JAVA-TP-009 START
    return new URL("http://api.internal.local/session?token=" + token).openConnection();
    // XG-BENCH:JAVA-TP-009 END
  }
}
