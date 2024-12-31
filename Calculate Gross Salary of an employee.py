import java.util.Scanner;
public class GrossSalaryCalculator 
{
    public static void main(String[] args)
     {
        Scanner A = new Scanner(System.in);
        float b = A.nextFloat();
        float H = A.nextFloat();
        float D = A.nextFloat();
        float P = 0.12f * b;
        float g = b + H + D+ P;
        System.out.printf("%.2f\n", P);
        System.out.printf("%.2f\n", g);
    }
}
