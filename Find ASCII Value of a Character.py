import java.util.Scanner;

public class ASCIIValue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        char ch = scanner.next().charAt(0);

        System.out.println((int) ch);

        scanner.close();
    }
}
