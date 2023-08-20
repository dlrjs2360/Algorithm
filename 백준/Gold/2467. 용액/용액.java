import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] arr;
    static int result;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        arr = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt).toArray();

        int left = 0, right = N - 1;
        int min = Integer.MAX_VALUE;
        int ansS = 0, ansE = 0;
        int sum;
        while (left < right) {
            sum = Math.abs(arr[left] + arr[right]);
            if (sum < min) {
                min = sum;
                ansS = left; ansE = right;
            }
            if (sum == 0) {break;}
            if (arr[left] + arr[right] > 0) right--;
            else left++;
        }
        System.out.println(arr[ansS]+" "+arr[ansE]);
    }

}