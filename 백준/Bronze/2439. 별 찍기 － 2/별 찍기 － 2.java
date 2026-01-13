import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        for (int i = 1; i <= N; i++) { // i : 1 ~ 5
            for (int j = N-i; j > 0; j--) { // j : 4 ~ 1
                System.out.print(' ');
            }
            for (int k = 1; k <= i; k++) {
                System.out.print('*');
            }
            System.out.println();
        }
    }
}