import java.util.Scanner;
public class SimpleInterest {
    public static void main(String[] args) 
    {
        Scanner A = new Scanner(System.in);
        int P = A.nextInt();  
        int T = A.nextInt();  
        int R = A.nextInt();  
        int SI = (P * T * R) / 100;
        System.out.println(SI);
    }
}
