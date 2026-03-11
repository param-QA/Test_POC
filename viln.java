import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class VulnerableApp {

    // 1. HARDCODED SECRETS (Should trigger 0xdea and gitleaks rules)
    private static final String DB_PASSWORD = "super_secret_password_123!";
    private static final String AWS_KEY = "AKIAJ2E34567890EXAMPLE"; 

    public void processData(String userInput) {
        try {
            // 2. SQL INJECTION (Should trigger OWASP / SAST Java rules)
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db", "admin", DB_PASSWORD);
            Statement stmt = conn.createStatement();
            String query = "SELECT * FROM users WHERE username = '" + userInput + "'";
            ResultSet rs = stmt.executeQuery(query);

            // 3. WEAK CRYPTOGRAPHY (DES is insecure - should trigger SAST rules)
            Cipher cipher = Cipher.Cipher.getInstance("DES"); 
            byte[] keyBytes = "12345678".getBytes();
            SecretKeySpec key = new SecretKeySpec(keyBytes, "DES");
            cipher.init(Cipher.ENCRYPT_MODE, key);
            
            // 4. SUSPICIOUS COMMENTS (Should trigger raptor-bad-words)
            // TODO: FIXME: This is a massive security BUG that we need to HACK a fix for later
            System.out.println("Processing complete.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
