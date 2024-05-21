import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class bj14888 {

    public static int maxValue = Integer.MIN_VALUE;
    public static int minValue = Integer.MAX_VALUE;
    public static int[] operator = new int[4];
    public static int[] numbers;
    public static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }
        for (int i = 0; i < 4; i++) {
            operator[i] = sc.nextInt();
        }
        solution(numbers[0], 1);
        System.out.println(maxValue);
        System.out.println(minValue);

    }
    public static void solution(int num, int index){
        if(index==N){
            maxValue = Math.max(maxValue,num);
            minValue = Math.min(minValue,num);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if(operator[i] > 0){
                operator[i]--;

                switch (i){
                    case 0:
                        solution(num + numbers[index], index + 1);
                        break;
                    case 1:
                        solution(num - numbers[index], index + 1);
                        break;
                    case 2:
                        solution(num * numbers[index], index + 1);
                        break;
                    case 3:
                        solution(num / numbers[index], index + 1);
                        break;
                }
                operator[i]++;
            }
        }
    }
}
