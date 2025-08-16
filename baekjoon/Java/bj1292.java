import java.util.Scanner;

public class bj1292 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int sum = 0;
        int index = 1;
        for (int i = 1; i <= B; i++) {
            for (int j = 0; j < i; j++) {
                if (A <= index && index <= B){
                    sum += i;
                }
                index++;
            }
        }
        System.out.println(sum);
    }
}
