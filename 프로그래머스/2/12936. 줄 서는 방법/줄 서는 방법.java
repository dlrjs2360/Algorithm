import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        LinkedList<Integer> l_list = new LinkedList();
        long ft = 1L;
        
        for (int i=1; i <= n; i++) {
            l_list.add(i);
            ft *= i;
        }

        k--;
        int idx = 0;
        while (n > 0) {
            ft /= n--;
            answer[idx++] = l_list.remove((int)(k / ft));
            k %= ft;
        }
        
        return answer;
    }
}