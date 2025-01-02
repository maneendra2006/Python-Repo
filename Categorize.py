import java.util.Scanner;
public class CategorizeHeight
 {
public static void main(String[] args)
 {
            Scanner scanner = new Scanner(System.in);
        
        double height = scanner.nextDouble();
            if (height < 150) {
            System.out.println("Person is Dwarf.");
        } else if (height <= 165) {
            System.out.println("Person is average heighted.");
        } else if (height <= 195) {
            System.out.println("Person is taller.");
        } else {
            System.out.println("Abnormal height.");
        }
           
    }
}
