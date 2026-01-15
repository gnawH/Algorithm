import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();
        int tmp = number;

        int left, right = 0;
        int result = -1;
        int count = 0;

        do {
            left = tmp / 10;
            right = tmp % 10;
            result = (right * 10) + ((left + right) % 10);

            tmp = result;
            count ++;
        } while (number != result);

        System.out.println(count);
    }
}