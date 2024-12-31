import java.util.Scanner;
public class TemperatureConversion 
{
    public static void main(String[] args) 
    {
        Scanner A = new Scanner(System.in);
        int c = A.nextInt();
        double f = 32 + (c * 9.0 / 5.0);
        System.out.printf("%.2f\n", f);
    }
}
