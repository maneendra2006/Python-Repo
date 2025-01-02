import java.util.Scanner;
public class Handshake
 {
public static void main(String[] args) 
{
        Scanner A = new Scanner(System.in);
        int n = A.nextInt();
        int handshakes = (n * (n - 1)) / 2;
        System.out.println(handshakes);
        
    }
}
