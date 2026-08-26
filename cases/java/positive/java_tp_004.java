import java.io.*;
class JavaTp004 {
  static Object load(InputStream in) throws Exception {
    // XG-BENCH:JAVA-TP-004 START
    ObjectInputStream ois = new ObjectInputStream(in);
    return ois.readObject();
    // XG-BENCH:JAVA-TP-004 END
  }
}
