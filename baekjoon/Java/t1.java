import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
public class t1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        String min_result = "";
        String max_result = "";
        Arrays.sort(input, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (Integer.parseInt(String.valueOf(o1.charAt(0))) > Integer.parseInt(String.valueOf(o2.charAt(0)))) {
                    return 1;
                }
                return 0;
            }
        });
        for (String s : input) {
            System.out.print(s);
        }
        System.out.println();
        for (String s : input) {
            max_result += s;
        }
        for (int i = input.length-1;i >=0; i--) {
            min_result += input[i];
        }
        System.out.println(Integer.parseInt(max_result) + Integer.parseInt(min_result));
    }
}
