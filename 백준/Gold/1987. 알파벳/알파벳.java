import java.io.IOException;
import java.util.*;
import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {
    static List<char[]> arr;
    static int[] dx = {1, 0, 0, -1};
    static int[] dy = {0, 1, -1, 0};
    static ArrayList<Character> item;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        // 입력 처리
        int s, r;
        s = Integer.parseInt(st2.nextToken());
        r = Integer.parseInt(st2.nextToken());

        arr = new ArrayList<>();
        for (int i = 0; i < s; i++) {
            StringTokenizer st3 = new StringTokenizer(br.readLine());
            arr.add(st3.nextToken().toCharArray());
        }

        item = new ArrayList<>();
        int res = dfs(0, 0, s, r);
        System.out.println(res);
    }
    static int dfs(int x, int y, int s, int r) {
        if (x >= s || x < 0 || y >= r || y < 0 || item.contains(arr.get(x)[y])) {
            return item.size();
        }

        item.add(arr.get(x)[y]);
        int L = 0;
        for (int i = 0; i < 4; i++) {
            L = Math.max(L, dfs(x+dx[i], y+dy[i], s, r));
        }
        item.remove(item.size() - 1);
        return L;
    }


}