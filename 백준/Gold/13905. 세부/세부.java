
import java.io.*;
import java.util.*;
public class Main {

    static int N, M;
    static int S, E;
    static PriorityQueue<Edge> heap;
    static int[] parent;

    public static int ancestor(int node) {
        if (node != parent[node]) parent[node] = ancestor(parent[node]);
        return parent[node];
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        heap = new PriorityQueue<>(Comparator.comparing(x -> -x.weight));
        for (int i = 0; i < M; i++) {
            heap.add(new Edge(Arrays.stream(
                br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray()));
        }

        parent = new int[N+1];
        for (int i = 1; i < N+1; i++) parent[i] = i;
        boolean status = false;
        while (!heap.isEmpty()) {
            Edge edge = heap.poll();
            int ps = ancestor(edge.start);
            int pe = ancestor(edge.end);
            if (ps == pe) continue;
            if (ps > pe) {
                int tmp = ps;
                ps = pe;
                pe = tmp;
            }
            parent[pe] = ps;
            if (ancestor(S) == ancestor(E)) {
                System.out.println(edge.weight);
                status = true;
                break;
            }
        }
        if (!status) {
            System.out.println(0);
        }

    }

    static class Edge {
        int start, end, weight;

        public Edge(int[] arr) {
            this.start = arr[0];
            this.end = arr[1];
            this.weight = arr[2];
        }
    }

}