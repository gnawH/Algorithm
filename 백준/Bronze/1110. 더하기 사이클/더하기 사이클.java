import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();
        int origin_num = number;
        int left, right = 0;
        int result = -1;
        int count = 0;

        while (origin_num != result) {
            // 10 이하 수, 전처리
            if (number < 10) {
                left = 0;
            } else {
                left = number / 10;
            }

            right = number % 10;

            result = (right * 10) + ((left + right) % 10);
            count ++;
            number = result;
        }
        System.out.println(count);
    }
}