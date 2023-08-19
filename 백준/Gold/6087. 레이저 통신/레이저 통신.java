import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int[] dx = {0, 1, -1, 0};
        int[] dy = {1, 0, 0, -1};
        int ax = 0;
        int ay = 0;
        int[][] graph = new int[H][W];

        for (int i = 0; i < H; i++) {
            String str = br.readLine();
            for (int j = 0; j < W; j++) {
                graph[i][j] = (str.charAt(j) == '.' ? -1 : (str.charAt(j) == '*') ? -2 : -3);
                if (graph[i][j] == -3) {
                    ax = i;
                    ay = j;
                }
            }
        }
        graph[ax][ay] = 0;
        PriorityQueue<Node> heap = new PriorityQueue<>(Comparator.comparingInt(x -> x.count));
        heap.add(new Node(0, ax, ay));

        last: while (!heap.isEmpty()) {
            Node node = heap.poll();
            for (int i = 0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                while (nx < H && nx >= 0 && ny < W && ny >= 0) {
                    int v = graph[nx][ny];
                    if (v == -3) { // C를 만났을 때
                        System.out.println(node.count);
                        break last;
                    }
                    else if (v == -2) { // 벽을 만났을 때
                        break;
                    }
                    else if (v == -1) { // 아직 한 번도 방문하지 않은 곳일 경우
                        graph[nx][ny] = node.count+1;
                        heap.add(new Node(node.count + 1, nx, ny));
                    }
                    else if (v >= 0 && v <= node.count) { // 이미 방문한 곳
                        break;
                    }
                    nx += dx[i];
                    ny += dy[i];
                }
            }
        }
    }

    public static class Node {
        int count, x, y;
        public Node(int count, int x, int y) {
            this.count = count;
            this.x = x;
            this.y = y;
        }
    }

}