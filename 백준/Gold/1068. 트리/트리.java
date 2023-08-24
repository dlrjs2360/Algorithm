import java.io.*;
import java.util.*;

public class Main {

    static int N,toRemove;
    static int[] parent;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        parent = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        toRemove = Integer.parseInt(br.readLine());

        DFS(toRemove);

        int answer = 0;
        for (int i = 0; i < N; i++) {
            boolean status = false;
            for (int p : parent) {
                if (p == i) status = true;
            }
            if (!status && parent[i] != -2) {
                answer++;
            }

        }

        System.out.println(answer);
    }

    public static void DFS(int node) {
        parent[node] = -2;
        for (int i = 0; i < N; i++) {
            if (parent[i] == node) DFS(i);
        }
    }

}