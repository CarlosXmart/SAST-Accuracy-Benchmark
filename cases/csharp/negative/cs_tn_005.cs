using System; using System.Net.Http; using System.Threading.Tasks;
class CsTn005 {
  public static async Task<string> Fetch(HttpClient c, string raw) {
    // XG-BENCH:CS-TN-005 START
    var u = new Uri(raw);
    if (u.Scheme != Uri.UriSchemeHttps || u.Host != "api.example.test") throw new InvalidOperationException();
    return await c.GetStringAsync(u);
    // XG-BENCH:CS-TN-005 END
  }
}
