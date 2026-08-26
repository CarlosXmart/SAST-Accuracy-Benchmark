using System.Security.Cryptography;
class CsTp006 {
  public static byte[] Hash(byte[] input) {
    // XG-BENCH:CS-TP-006 START
    using var md5 = MD5.Create(); return md5.ComputeHash(input);
    // XG-BENCH:CS-TP-006 END
  }
}
