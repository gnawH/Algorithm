import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 2007. 1. 1 (MON)
        String[] week = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        // 31 = {1, 3, 5, 7, 8, 10, 12} (월)
        // 30 = {4, 6, 9, 11} (월)
        // 28 = {2} (월)
        int[] days_amount = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int month = sc.nextInt();
        int day = sc.nextInt();
        int sum = 0;

        for (int i = 1; i < month; i++) {
            sum += days_amount[i];
        }
        System.out.println(week[(sum + day) % 7]);
    }
}