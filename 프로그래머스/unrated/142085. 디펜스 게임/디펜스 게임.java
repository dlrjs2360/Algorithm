import java.util.*;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> past = new PriorityQueue<>(Collections.reverseOrder());
        for (int e: enemy){
            past.add(e);
            if (n >= e){
                n -= e;
                answer++;
                continue;
            }
            while (k > 0 && n < e && !past.isEmpty()){
                n += past.poll();
                k--;
            }
            if (n >= e){
                n -= e;
                answer++;
                continue;
            }
            break;
        }
        return answer;
    }
}