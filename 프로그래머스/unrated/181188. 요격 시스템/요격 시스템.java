import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int limit = 0;
        Arrays.sort(targets,Comparator.comparing((int[] a) -> a[0]).thenComparing((int[] a) -> a[1]));
        for (int[] t: targets){
            int left = t[0];
            int right = t[1];
            if (right <= limit){
                limit = right;
            }
            else if (left >= limit){
                answer ++;
                limit = right;
            }
        }
        
        //System.out.println(Arrays.deepToString(targets));
        
        return answer;
    }
}