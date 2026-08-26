using System.Text.Json;
class CsTn004 {
  public static object? Load(string input) {
    // XG-BENCH:CS-TN-004 START
    return JsonSerializer.Deserialize<object>(input);
    // XG-BENCH:CS-TN-004 END
  }
}
