import java.util.Scanner;
public class OctalToBinary 
{
    public static void main(String[] args)
     {
        Scanner A = new Scanner(System.in);
        int Q = A.nextInt();
        for (int i = 0; i < Q; i++) 
        {
            String octal = A.next();
            int decimal = Integer.parseInt(octal, 8);
            System.out.println(Integer.toBinaryString(decimal));
        }
    }
}
