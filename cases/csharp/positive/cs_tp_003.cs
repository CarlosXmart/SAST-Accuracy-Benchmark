using System.Data.SqlClient;
class CsTp003 {
  public static SqlCommand Query(SqlConnection c, string user) {
    // XG-BENCH:CS-TP-003 START
    return new SqlCommand("SELECT * FROM users WHERE name='" + user + "'", c);
    // XG-BENCH:CS-TP-003 END
  }
}
