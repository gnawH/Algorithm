import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] count = new int[10];

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int result = A * B * C;

        String str_num = Integer.toString(result);

        for (int i = 0; i < str_num.length(); i++) {
            count[str_num.charAt(i) - '0']++;
        }

        for (int n : count) {
            System.out.println(n);
        }
    }
}