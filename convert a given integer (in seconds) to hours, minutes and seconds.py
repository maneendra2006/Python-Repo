import java.util.Scanner;
public class TimeConversion
 {
    public static void main(String[] args)
     {
        Scanner A = new Scanner(System.in);
        int t = A.nextInt();
        int h = t / 3600;
        int r = t % 3600;
        int m = r / 60;
        int s = r % 60;
        System.out.println("H:M:S-" + h + ":" + m + ":" + s);
    }
}
