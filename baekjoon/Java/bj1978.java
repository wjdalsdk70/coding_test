import java.util.Scanner;

public class bj1978 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int cnt = 0;
            for (int j = 1; j < a; j++) {
                if(a%j==0) cnt++;
            }
            if (cnt==1){
                count += 1;
            }
        }
        System.out.println(count);
    }
}
