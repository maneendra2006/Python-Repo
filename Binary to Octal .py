import java.util.Scanner;
public class BinaryToOctal 
{
    public static void main(String[] args) 
    {
        Scanner A = new Scanner(System.in);
        int Q = A.nextInt();
        A.nextLine();  
        for (int i = 0; i < Q; i++)
         {
            String binaryNumber = A.nextLine();
            int decimal = Integer.parseInt(binaryNumber, 2);
            String octal = Integer.toOctalString(decimal);
            System.out.println(octal);
        }
    }
}
