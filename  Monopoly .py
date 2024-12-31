import java.util.Scanner;
public class Monopoly {
    public static void main(String[] args) {
        Scanner A = new Scanner(System.in);
        int T = A.nextInt();
        for (int i = 0; i < T; i++) {
            int R1 = A.nextInt();
            int R2 = A.nextInt();
            int R3 = A.nextInt();
            if (R1 > R2 + R3 || R2 > R1 + R3 || R3 > R1 + R2) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
