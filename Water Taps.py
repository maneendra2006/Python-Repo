import java.util.Scanner;
public class WaterTaps
 {
    public static void main(String[] args)
    {
        Scanner A = new Scanner(System.in);
        int X = A.nextInt(); 
        int Y = A.nextInt();  
        int B = (X * Y) / (X + Y);
        System.out.println(B);
    }
}
