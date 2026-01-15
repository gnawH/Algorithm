import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String text = sc.nextLine().strip();
        int length = text.length();
        int count = 0;
        
        if (length > 0) {
            for (int i = 0; i < text.length(); i++) {
                if (text.charAt(i) == 32) {
                    count ++;
                }
            }
            count ++;
        }
        System.out.println(count);
    }
}