import java.sql.Statement;

public class vuln {
    public void test(Statement st, String id) throws Exception {
        // This line triggers the java-sqli-test rule 
        // because it uses string concatenation (+) inside executeQuery()
        st.executeQuery("SELECT * FROM users WHERE id = " + id);
    }
}
