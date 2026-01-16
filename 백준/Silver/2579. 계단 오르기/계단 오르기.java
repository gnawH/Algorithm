import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 계단의 수
        int[] stairs = new int[N];  // 계단별 점수 저장 배열

        for (int i = 0; i < N; i++) {
            stairs[i] = sc.nextInt();
        }

        int[] dp = new int[N];  // 계단별 최대값 저장 배열

        if (N >= 1) {
            dp[0] = stairs[0];
        }
        if (N >= 2) {
            dp[1] = stairs[0] + stairs[1];
        }
        if (N >= 3) {
            dp[2] = Math.max(stairs[2] + stairs[0], stairs[2] + stairs[1]);
        }
        if (N > 3) {
            for (int i = 3; i < N; i++) {
                dp[i] = Math.max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2]);
            }
        }

        System.out.println(dp[N-1]);
    }
}