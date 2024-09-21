import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer;
        
        int left = 0;
        int right = Arrays.stream(diffs).max().getAsInt();
        long tmp;
        answer =  (left + right) / 2;
        
        while (left < answer && answer < right) {
            tmp = calCost(answer ,diffs, times, limit);
            if (tmp <= limit) { // answer을 낮춤.
                right = answer;
                answer = (right+left) / 2;
            } else { // answer을 높임.
                left = answer;
                answer = (right+left) / 2;
            }
        }
        
        return answer+1;
    }
    
    long calCost(int level, int[] diffs, int[] times, long limit) {
        long res = 0;
        for (int i = 0; i < diffs.length; i++) {
            int d = diffs[i];
            int t = times[i];
            
            if (d <= level) {
                res += t;
            } else {
                res += t * (d-level+1);
                if (i > 0) {
                    res += times[i-1] * (d-level); 
                }
            }
        }
        
        return res;
    }
}