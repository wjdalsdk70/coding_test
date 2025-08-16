import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class test {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        String min_result = "";
        String max_result = "";
        for (String s : input) {
            max_result += s;
        }
        for (int i = input.length-1;i >=0; i--) {
            min_result += input[i];
        }
        System.out.println(Integer.parseInt(max_result));
        System.out.println(Integer.parseInt(min_result));
        System.out.println(Integer.parseInt(max_result) + Integer.parseInt(min_result));
    }
}
