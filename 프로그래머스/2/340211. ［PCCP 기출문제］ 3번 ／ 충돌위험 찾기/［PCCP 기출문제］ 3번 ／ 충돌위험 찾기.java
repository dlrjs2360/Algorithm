import java.util.*;

class Solution {
    public int solution(int[][] points, int[][] routes) {
        int[] start, end;
        boolean[][][] visit = new boolean[100000][101][101];
        Set<String> dpTime = new HashSet();
        int t;
        int x,y;
        
        for (int[] edge: routes) {
            t = 0;
            for (int i = 0; i < edge.length-1; i++) {        
                start = points[edge[i]-1];
                end = points[edge[i+1]-1];
                
                List<int[]> route = findRoute(start, end, i);
                
                for (int[] r: route) {
                    x = r[0];
                    y = r[1];
                    
                    //System.out.println(x + " " + y);
                    if (visit[t][x][y]) {
                        String s = t+"+"+x+"+"+y;
                        dpTime.add(s);
                    }
                    else {
                        visit[t][x][y] = true;
                    }
                    t++;
                }
            }
        }
        
        return dpTime.size();
    }
    
    public List<int[]> findRoute(int[] A, int[] B, int i) {
        List<int[]> route = new ArrayList();
        if (i == 0) {
            route.add(A);
        }
        int x = A[0];
        int y = A[1];
        while (x != B[0]) {
            if (B[0] > x) { x++; } 
            else{ x--; }
            route.add(new int[]{x,y});
        }
        
        while (y != B[1]) {
            if (B[1] > y) { y++; } 
            else { y--; }
            route.add(new int[]{x,y});
        }
        
        return route;
    }
}