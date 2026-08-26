import javax.crypto.Cipher;
class JavaTn007 {
  static Cipher cipher() throws Exception {
    // XG-BENCH:JAVA-TN-007 START
    return Cipher.getInstance("AES/GCM/NoPadding");
    // XG-BENCH:JAVA-TN-007 END
  }
}
