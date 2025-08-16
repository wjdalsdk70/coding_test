import java.util.Scanner;

public class bj2581 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int sum = 0;
        int min_n = 10001;
        for (int i = M; i <= N; i++) {
            if(judge(i)){
                if (min_n > i) min_n = i;
                sum += i;
            }
        }
        if(sum == 0){
            System.out.println(-1);
        }else {
            System.out.println(sum);
            System.out.println(min_n);
        }
    }

    public static boolean judge(int n){
        int count = 0;
        for (int i = 1; i < n; i++) {
            if(n%i == 0) count+=1;
        }
        if(count==1) return true;
        return false;
    }
}
