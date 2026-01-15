import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int X = sc.nextInt();
        String result = "";

        for (int i = 1; i <= N; i++) {
            int number = sc.nextInt();

            if (number < X) {
                result += Integer.toString(number);
                result += " ";
            }
        }

        System.out.println(result);

    }
}