import java.util.Scanner;
public class HexToBinary
 {
    public static void main(String[] args)
     {
        Scanner A = new Scanner(System.in);
        int Q = A.nextInt();
        A.nextLine();  
        for (int i = 0; i < Q; i++)
         {
            String hexa = A.nextLine();
            int decimal = Integer.parseInt(hexa, 16);
            String binary = Integer.toBinaryString(decimal);
            int reqlen = hexa.length() * 4;
            while (binary.length() < reqlen) {
                binary = "0" + binary;
            }
                System.out.println(binary);
        }
    }
}
