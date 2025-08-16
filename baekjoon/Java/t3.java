import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class t3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        System.out.println("Hello Goorm! Your input is " + input);
    }
}
