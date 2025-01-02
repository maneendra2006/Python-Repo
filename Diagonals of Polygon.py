import java.util.Scanner;
public class DiagonalsOfPolygon 
{
public static void main(String[] args) {
        Scanner A = new Scanner(System.in);
        int N = A.nextInt();
        int d = (N * (N - 3)) / 2;
        System.out.println(d);
    }
}
