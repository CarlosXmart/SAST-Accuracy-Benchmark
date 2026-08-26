import java.io.*;
class JavaTn004 {
  static String load(InputStream in) throws Exception {
    // XG-BENCH:JAVA-TN-004 START
    return new DataInputStream(in).readUTF();
    // XG-BENCH:JAVA-TN-004 END
  }
}
