import java.sql.*;

public class SQLi {
    public void doGet(String userId, Connection conn) throws Exception {
        Statement statement = conn.createStatement();
        // Trigger: User input directly concatenated into SQL query
        String query = "SELECT * FROM users WHERE id = '" + userId + "'";
        ResultSet rs = statement.executeQuery(query);
    }
}
