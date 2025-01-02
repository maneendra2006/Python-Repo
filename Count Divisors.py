import java.util.Scanner;
public class CountDivisors 
{
public static void main(String[] args) {
        Scanner A = new Scanner(System.in);
        int l = A.nextInt();
        int r = A.nextInt();
        int k = A.nextInt();
        int c = (r / k) - ((l - 1) / k);
        System.out.println(c);
    }
}
