using System.Net;
class CsTp005 {
  public static string Fetch(string url) {
    // XG-BENCH:CS-TP-005 START
    return new WebClient().DownloadString(url);
    // XG-BENCH:CS-TP-005 END
  }
}
