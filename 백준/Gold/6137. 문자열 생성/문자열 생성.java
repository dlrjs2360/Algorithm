
import java.io.*;
import java.util.*;

public class Main {

    static int N;

    static String S;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        N = Integer.parseInt(br.readLine());
        S = "";
        for (int i = 0; i < N; i++) {
            S = S.concat(br.readLine());
        }
        char[] answer = new char[N];
        int idx = 0;
        while (!S.isEmpty()) {
            int left = 0, right = S.length() - 1;
            int left_v = left, right_v = right;
            while (S.charAt(left_v) == S.charAt(right_v) && left_v < right_v) {
                left_v++; right_v--;
            }
            if (S.charAt(left_v) > S.charAt(right_v)) {
                answer[idx] = S.charAt(right);
                S = S.substring(0, right);
            } else {
                answer[idx] = S.charAt(left);
                S = S.substring(1);
            }
            idx++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < answer.length; i++) {
            if (i % 80 == 0 && i > 0) sb.append("\n");
            sb.append(answer[i]);
        }
        System.out.println(sb);
    }

}