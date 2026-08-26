import java.sql.*;
class JavaTp001 {
  static ResultSet find(Statement st, String user) throws Exception {
    // XG-BENCH:JAVA-TP-001 START
    String sql = "SELECT * FROM users WHERE name='" + user + "'";
    return st.executeQuery(sql);
    // XG-BENCH:JAVA-TP-001 END
  }
}
