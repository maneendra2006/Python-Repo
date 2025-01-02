import java.util.Scanner;
public class CelsiusToFahrenheit
 {
public static void main(String[] args)
 {
        Scanner A = new Scanner(System.in);
        int c = A.nextInt();
        double f = (9.0 / 5.0) * c + 32;
        System.out.printf("%.2f\n", f);
    }
}
