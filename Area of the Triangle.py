import java.util.Scanner;
public class TriangleArea 
{
    public static void main(String[] args)
     {
        Scanner A = new Scanner(System.in);
        double a = A.nextDouble();
        double b = A.nextDouble();
        double c = A.nextDouble();
        double s = (a + b + c) / 2;
        double area = Math.sqrt(s * (s - a) * (s - b) * (s - c));
        System.out.printf("%.2f\n", area);
    }
}
