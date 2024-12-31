import java.util.Scanner;
public class OctalToDecimal
{
    public static void main(String[] args) 
    {
        Scanner A = new Scanner(System.in);
        String  o = A.nextLine();
        int d = Integer.parseInt(o, 8);
        System.out.println(d);
    }
}
