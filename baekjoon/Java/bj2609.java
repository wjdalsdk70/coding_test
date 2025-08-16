import java.util.Scanner;

public class bj2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int d = gcd(a,b);
        System.out.println(gcd(a,b));
        System.out.println(a*b/d);
    }
    public static int gcd(int a, int b){
        while (b > 0) {
            int temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }
}
