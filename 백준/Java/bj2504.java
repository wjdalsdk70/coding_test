import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class bj2504 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        Stack<Character> st = new Stack<>();

        int result = 0;
        int tmp = 1;

        L1 : for (int i = 0; i < input.length(); i++) {
                char c = input.charAt(i);
                switch (c){
                    case '(':
                        st.add(c);
                        tmp *= 2;
                        break;
                    case '[':
                        st.add(c);
                        tmp *= 3;
                        break ;
                    case ')':
                        if(st.empty() || st.peek()!='('){
                            result = 0;
                            break L1;
                        }else{

                        }
                }
            }
    }
}
