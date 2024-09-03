import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        // 트리 구조 생성하기
        HashMap<Integer,List<Integer>> map = new HashMap<>(); 
        HashMap<Integer,Boolean> visit = new HashMap<>();
        
        for (int i = 0; i <= n; i++) {
            map.put(i,new ArrayList<Integer>());
            visit.put(i, false);
        }
        
        for (int[] w : wires) {
            
            int a = w[0];
            int b = w[1];
            map.get(a).add(b);
            map.get(b).add(a);
        }
        
        // 정답 구하기
        for (int[] w: wires) {
            int a = w[0];
            int b = w[1];
            
            answer = Math.min(answer, Math.abs(getSum(map,a,b) - getSum(map,b,a)));
            
        }
        return answer;
    }
    
    // 개수 구하기
    int getSum(HashMap<Integer,List<Integer>> map, int start, int forbidden) {
        int res = 1;
        
        HashMap<Integer,Boolean> visit = new HashMap<>();
        
        visit.putIfAbsent(start, true);
        visit.putIfAbsent(forbidden, true);
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int next: map.get(node)) {
                if (visit.containsKey(next) && visit.get(next)) { continue; }
                res += 1;
                queue.add(next);
                visit.putIfAbsent(next,true);
            }
        }
    
        return res;
        
    }
    

}