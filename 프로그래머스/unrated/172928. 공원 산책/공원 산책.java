import java.util.*;

class Solution {
    public int[] solution(String[] park, String[] routes) {
        int lx = park.length;
        int ly = park[0].length();
        int[][] base = {
            {1,0},{-1,0},{0,-1},{0,1}
        };
        HashMap<String,int[]> direction = new HashMap<>();
        direction.put("S",base[0]);
        direction.put("N",base[1]);
        direction.put("W",base[2]);
        direction.put("E",base[3]);
        
        int[] prev = new int[2];
        for (int i=0; i<lx; i++){
            for (int j =0; j < ly; j++){
                if (park[i].charAt(j) == 'S'){
                    prev[0] = i;
                    prev[1] = j;
                    break;
                }
            }
        }
        
        for (String r: routes){
            String[] sp = r.split(" ");
            int[] d = direction.get(sp[0]);
            int c = Integer.parseInt(sp[1]);
            if (prev[0]+d[0]*c >= lx | prev[1]+d[1]*c >= ly | prev[0]+d[0]*c < 0 | prev[1]+d[1]*c < 0){
                continue;
            }
    
            boolean status = false;
            for (int i = 1; i <= c; i++){
                if (park[prev[0]+i*d[0]].charAt(prev[1]+i*d[1]) == 'X'){
                    status = true;
                    break;
                }
            }
            if (status){
                continue;
            }
            prev[0] += d[0]*c;
            prev[1] += d[1]*c;
        }
        
        return prev;
    }
}