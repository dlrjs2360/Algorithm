import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        
        int answer = Integer.MAX_VALUE;
        
        int lx = maps.length;
        int ly = maps[0].length;
        
        Queue<int[]> queue = new LinkedList();
        int[] start = {0,0,1};
        queue.add(start);
        
        boolean[][] visit = new boolean[lx][ly];
        visit[0][0] = true;
        
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        
        while (!queue.isEmpty()){
            int[] node = queue.poll();
            //System.out.println(Arrays.toString(node));
            if (node[0] == lx-1 && node[1] == ly-1){
                answer = Math.min(answer,node[2]);
                continue;
            }
            for (int i=0; i < 4; i++){
                int nx = node[0]+dx[i];
                int ny = node[1]+dy[i];
                if (nx < lx && nx >= 0 && ny < ly && ny >= 0 && maps[nx][ny] != 0 && !visit[nx][ny]){
                    visit[nx][ny] = true;
                    int[] nextNode = {nx,ny,node[2]+1};
                    queue.add(nextNode);
                }
            }
        }
        if (answer >= Integer.MAX_VALUE){
            return -1;
        }
        return answer;
    }
}