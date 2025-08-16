import java.util.Arrays;
import java.util.Scanner;

public class bj2309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }
        int exA = 0;
        int exB = 0;
        for (int i : arr) {
            for (int j : arr) {
                if(i!=j && sum - i - j == 100){
                    exA = i;
                    exB = j;
                }
            }
        }
        Arrays.sort(arr);
        for (int i : arr) {
            if (i!=exA&&i!=exB){
                System.out.println(i);
            }
        }
    }
}
