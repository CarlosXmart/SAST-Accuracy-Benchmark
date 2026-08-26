import java.net.*; import java.io.*;
class JavaTn006 {
  static InputStream fetch(String raw) throws Exception {
    // XG-BENCH:JAVA-TN-006 START
    URI u = URI.create(raw).normalize();
    if (!"https".equalsIgnoreCase(u.getScheme()) || !"api.example.test".equalsIgnoreCase(u.getHost()))
      throw new SecurityException("blocked destination");
    return u.toURL().openStream();
    // XG-BENCH:JAVA-TN-006 END
  }
}
