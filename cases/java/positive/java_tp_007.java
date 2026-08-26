import javax.crypto.Cipher;
class JavaTp007 {
  static Cipher cipher() throws Exception {
    // XG-BENCH:JAVA-TP-007 START
    return Cipher.getInstance("DES/ECB/PKCS5Padding");
    // XG-BENCH:JAVA-TP-007 END
  }
}
