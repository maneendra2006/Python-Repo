import java.util.Scanner;
public class FahrenheitToCelsius
 {
 public static void main(String[] args) {
        Scanner A = new Scanner(System.in);
        int f = A.nextInt();
        double c = (5.0 / 9.0) * (f - 32);
        System.out.printf("%.2f\n", c);
    }
}
