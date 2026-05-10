import java.security.MessageDigest;

public class MD5{

    public static void main(String[] args) throws Exception{

        String text = "Hello";
        
        MessageDigest md = MessageDigest.getInstance("MD5");

        // Converting text to bytes
        md.update(text.getBytes());

        // creating the hash
        byte[] hash = md.digest();

        // Printing
        System.out.println("The Original text is : " + text);

        System.out.println("The MD5 Hash value is : ");

        for (byte b : hash){
            System.out.printf( "%02X" ,b);
        }

    }
}