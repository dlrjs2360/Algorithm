import java.util.*;

class Solution {
    
    List<Integer> answer = new LinkedList<>();
    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};
    int lx, ly;
    boolean[][] visit;
    
    public int[] solution(String[] maps) {
        lx = maps.length;
        ly = maps[0].length();
        visit = new boolean[lx][ly];
        for (int i = 0; i < lx; i++){
            for (int j = 0; j < ly; j++){
                if (maps[i].charAt(j) != 'X' && !visit[i][j]) bfs(i,j,maps);
            }
        }
        if (answer.isEmpty()) {
            int[] answer2 = {-1};
            return answer2;
        }
        Collections.sort(answer);
        return answer.stream().mapToInt(i->i).toArray();
    }
    
    public void bfs(int i, int j, String[] maps){
        int total = maps[i].charAt(j) - '0';
        Queue<int[]> queue = new LinkedList<>();
        int[] start = {i,j};
        visit[i][j] = true;
        queue.add(start);
        while (!queue.isEmpty()){
            int[] node = queue.poll();
            int x = node[0];
            int y = node[1];
            for (int h = 0; h < 4; h++){
                int nx = x + dx[h];
                int ny = y + dy[h];
                if (check(nx,ny,maps)){
                    total += maps[nx].charAt(ny) - '0';
                    visit[nx][ny] = true;
                    int[] nextNode = {nx,ny};
                    queue.add(nextNode);
                }
            }
        }
        answer.add(total);
    }
    
    public boolean check(int x, int y, String[] maps) {
        return (x < lx && x >= 0 && y < ly && y >= 0 && !visit[x][y] && maps[x].charAt(y) != 'X');
    }
}