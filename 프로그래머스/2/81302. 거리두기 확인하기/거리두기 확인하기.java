import java.util.*;

class Solution {
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        int idx = 0;
        boolean status;
        
        for (String[] p: places) {
            status = true;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (p[i].charAt(j) == 'P') {
                        status = check(p, i, j);
                    }
                    if (!status) {break;}
                }
                if(!status) {break;}
            }
            
            if (status) {answer[idx] = 1;}
            else {answer[idx] = 0;}
            
            idx++;
        }
        
        return answer;
    }
    
    boolean check(String[] p, int x, int y) {
        int[] dx = {1, 0, 0 ,-1};
        int[] dy = {0, 1, -1, 0};
        
        boolean[][] visit = new boolean[5][5];
        
        Queue<Node> queue = new LinkedList();
        queue.add(new Node(x,y,0));
        visit[x][y] = true;
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            if (node.dist >= 2) {continue;}
            for (int i=0; i < 4; i++) {
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                
                if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5 || visit[nx][ny]) {
                    continue;
                }
                
                char nv = p[nx].charAt(ny);
                
                if (nv == 'P') {
                    return false;
                } else if (nv == 'O') {
                    queue.add(new Node(nx,ny,node.dist+1));
                    visit[nx][ny] = true;
                }
            }
        }
        return true;
    }
    
    class Node {
        int x, y, dist;
        
        public Node (int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
        
    }
}