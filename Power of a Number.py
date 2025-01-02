import java.util.Scanner;
public class PowerMod 
{
public static long modPower(int x, int y, int m) {
        long result = 1; 
        x = x % m;  
        while (y > 0) {
            if (y % 2 == 1) {
                result = (result * x) % m;
            }
            x = (x * x) % m;
            y = y / 2;
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int m = scanner.nextInt();
        
        long result = modPower(x, y, m);
        
        System.out.println(result);
        
        
    }
}
