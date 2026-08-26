using System.Data.SqlClient;
class CsTn003 {
  public static SqlCommand Query(SqlConnection c, string user) {
    // XG-BENCH:CS-TN-003 START
    var cmd = new SqlCommand("SELECT * FROM users WHERE name=@name", c);
    cmd.Parameters.AddWithValue("@name", user); return cmd;
    // XG-BENCH:CS-TN-003 END
  }
}
