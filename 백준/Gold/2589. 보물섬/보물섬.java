
import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static List<List<String>> graph;

    static int answer = 0;
    static int[] dx = {0, 1, -1, 0};
    static int[] dy = {1, 0, 0, -1};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i < N; i++) graph.add(List.of(br.readLine().split("")));
        List<List<Boolean>> visit = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            visit.add(new ArrayList<>());
            for (int j = 0; j < M; j++) {
                visit.get(i).add(false);
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (graph.get(i).get(j).equals("W")) continue;
                for (int k = 0; k < N; k++) {
                    visit.get(k).replaceAll((x) -> false);
                }
                Deque<Node> queue = new ArrayDeque<>();
                queue.add(new Node(0, i, j));
                visit.get(i).set(j, true);
                while (!queue.isEmpty()) {
                    Node node = queue.pollFirst();
                    if (node.distance > answer) answer = node.distance;
                    for (int k = 0; k < 4; k++) {
                        int nx = node.x + dx[k];
                        int ny = node.y + dy[k];
                        if (nx >= N || nx < 0 || ny >= M || ny < 0
                            || visit.get(nx).get(ny)
                            || graph.get(nx).get(ny).equals("W")) continue;
                        queue.addLast(new Node(node.distance + 1, nx, ny));
                        visit.get(nx).set(ny, true);
                    }
                }
            }
        }
        System.out.println(answer);
    }
    static class Node{

        int distance,x,y;

        public Node(int distance, int x, int y) {
            this.distance = distance;
            this.x = x;
            this.y = y;
        }
    }

}