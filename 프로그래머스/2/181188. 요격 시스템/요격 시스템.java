import java.util.*;

class Solution {
    public int solution(int[][] t) {
        int answer = 0;
    
        Arrays.sort(t,new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return (a[0] == b[0] )? a[1]-b[1] : a[0]-b[0];
            }
        });
        
        int ml = 0, mr = 0;
        for (int i = 0; i < t.length; i++) {
            if (mr <= t[i][0]) {
                answer ++;
                ml = t[i][0];
                mr = t[i][1];
            } else {
                mr = Math.min(mr, t[i][1]);
            }
        }
        
        
        return answer;
    }
}