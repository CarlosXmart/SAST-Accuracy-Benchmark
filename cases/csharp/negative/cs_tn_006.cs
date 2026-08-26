using System.Security.Cryptography;
class CsTn006 {
  public static byte[] Hash(byte[] input) {
    // XG-BENCH:CS-TN-006 START
    using var sha = SHA256.Create(); return sha.ComputeHash(input);
    // XG-BENCH:CS-TN-006 END
  }
}
