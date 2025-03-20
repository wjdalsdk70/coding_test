import java.util.Arrays;
import java.util.Scanner;

public class bj14719 {
    public static int H;
    public static int W;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        H = sc.nextInt();
        W = sc.nextInt();
        int[][] arr = new int[H][W];
        for (int i = 0; i < W; i++) {
            int n = sc.nextInt();
            for (int j = 0; j < n; j++) {
                arr[n-j-1][i] = 1;
            }
        }
        int count = 0;
        for (int i = 1; i < W-1; i++) {
            for (int j = 0; j < H; j++) {
                if (isaBoolean(i, arr[j])) {
                    System.out.print(j);
                    System.out.print(i);
                    System.out.println();
                    count++;
                }
            }
        }
        System.out.println(count);
    }

    public static boolean isaBoolean(int i, int[] arr) {
        boolean left = false;
        boolean right = false;
        for (int j = 0; j <i; j++) {
            if (arr[j]==1){
                left = true;
            }
        }
        for (int j = i+1; j < W; j++) {
            if (arr[j]==1){
                right = true;
            }
        }
        if (left && right) return true;
        return false;
    }
}
