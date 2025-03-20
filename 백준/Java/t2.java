import java.io.BufferedReader;
import java.io.InputStreamReader;

public class t2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        if(input[0].equals("encrypt")){
            System.out.println(encrypt(input));

        }else{
            System.out.println(decrypt(input));
        }
    }

    private static String encrypt(String[] input) {
        int[] arr = new int[input[1].length()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (input[1].charAt(i)-'a') + (input[3].charAt(i)-'a');
        }
        if(Integer.parseInt(input[2]) > 0)
            arr = leftshift(Integer.parseInt(input[2]), arr);
        else {
            arr = rightshift(Math.abs(Integer.parseInt(input[2])), arr);
        }
        String result = "";
        for (int i : arr) {
            result += (char)(i + 'a');
        }
        return result;
    }

    private static String decrypt(String[] input) {
        int[] arr = new int[input[3].length()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = input[3].charAt(i)-'a';
        }
        if(Integer.parseInt(input[2]) > 0)
            arr = rightshift(Integer.parseInt(input[2]), arr);
        else {
            arr = leftshift(Integer.parseInt(input[2]), arr);
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] -= input[1].charAt(i)-'a';
        }
        String result = "";
        for (int i : arr) {
            result += (char)(Math.abs(i) + 'a');
        }
        return result;
    }

    private static int[] rightshift(int a, int[] arr) {
        for(int i =0; i < a; i++){
            int last = arr[arr.length - 1];

            for(int j = arr.length-1; j > 0; j--){
                arr[j] = arr[ j - 1];
            }
            arr[0] = last;
        }
        return arr;
    }

    private static int[] leftshift(int a, int[] arr) {
        for(int i = 0; i < a; i++){
            int temp = arr[0];

            for(int j = 0; j < arr.length - 1; j++){
                arr[j] = arr[j+1];
            }
            arr[arr.length - 1] = temp;
        }
        return arr;
    }

}
