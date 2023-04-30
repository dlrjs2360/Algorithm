import java.util.*;
class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        for (int x: section) {
            queue.add(x);
        }
        while (!queue.isEmpty()) {
            int fillOut = queue.poll()+m-1;
            while (!queue.isEmpty() && queue.peek() <= fillOut) {
                queue.poll();
            }
            answer ++;
        }
        return answer;
    }
}