import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String words = sc.nextLine();
        for (int i = 0; i < words.length(); i++) {
            if (i > 0 && i % 10 == 0) {
                System.out.println();
            }
            System.out.print(words.charAt(i));
        }
    }
}