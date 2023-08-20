import java.io.*;
import java.util.*;

public class Main {

    static int L, C;
    static String[] arr;
    static List<String> moum;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = br.readLine().split(" ");
        Arrays.sort(arr);
        moum = new ArrayList<>(){{
            add("a");
            add("e");
            add("i");
            add("o");
            add("u");
        }};
        for (int i = 0; i < C; i++) {
            if (moum.contains(arr[i])) {
                DFS(arr[i], 1 << i, 1, 0);
                continue;
            }
            DFS(arr[i], 1 << i, 0, 1);
        }
    }

    public static void DFS(String total, int visit, int m, int n) {
        if (total.length() == L && m >= 1 && n >= 2) {
            System.out.println(total);
            return;
        }
        for (int j = 0; j < C; j++) {
            if ((visit & (1 << j)) == (1 << j)
                || total.charAt(total.length()-1) >= arr[j].charAt(0)
            ) continue;

            if (moum.contains(arr[j])) {
                DFS(total.concat(arr[j]), visit | (1 << j), m + 1, n);
            }
            else{
                DFS(total.concat(arr[j]), visit | (1 << j), m, n+1);
            }

        }
    }
}