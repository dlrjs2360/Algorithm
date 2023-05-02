import java.util.*;

class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        
        int[][] dist = new int[n+1][n+1];
        for (int i=1; i<n+1; i++){
            Arrays.fill(dist[i],20000001);
            dist[i][i] = 0;
        }
        
        for (int[] f: fares){
            int x = f[0];
            int y = f[1];
            int w = f[2];
            dist[x][y] = w;
            dist[y][x] = w;
        }
        
        // 플로이드-워샬
        for (int k=1; k<n+1; k++){
            for (int i=1; i<n+1; i++){
                for (int j=1; j<n+1; j++){
                    dist[i][j] = Math.min(dist[i][j],dist[i][k]+dist[k][j]);
                }
            }
        }
        
        int answer = Integer.MAX_VALUE;
        for (int i=1; i<n+1; i++){
            answer = Math.min(dist[s][i]+dist[i][a]+dist[i][b], answer);
        }
        
        return answer;
    }
}