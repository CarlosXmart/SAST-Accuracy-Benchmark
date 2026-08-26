import java.sql.*;
class JavaTn001 {
  static ResultSet find(Connection c, String user) throws Exception {
    // XG-BENCH:JAVA-TN-001 START
    PreparedStatement ps = c.prepareStatement("SELECT * FROM users WHERE name=?");
    ps.setString(1, user);
    return ps.executeQuery();
    // XG-BENCH:JAVA-TN-001 END
  }
}
