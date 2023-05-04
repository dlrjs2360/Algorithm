import java.util.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        for (int i = 0; i<wires.length; i++){  
            HashMap<Integer,ArrayList<Integer>> graph = new HashMap();
            for (int j = 0; j < n+1; j++) graph.put(j+1,new ArrayList<Integer>());
            
            for (int j = 0; j < wires.length; j++){
                if (i ==j) continue;
                int[] wire = wires[j];
                graph.get(wire[0]).add(wire[1]);
                graph.get(wire[1]).add(wire[0]);
            }
            
            boolean[] visit = new boolean[n+1];
            
            int node_a = wires[i][0];
            visit[node_a] = true;
            Queue<Integer> queue_a = new LinkedList();
            queue_a.add(node_a);
            int cnt_a = 1;
            while(!queue_a.isEmpty()){
                int node = queue_a.poll();
                for (int nextNode: graph.get(node)){
                    if (!visit[nextNode]){
                        queue_a.add(nextNode);
                        cnt_a++;
                        visit[nextNode] = true;
                    }
                }
            }
            
            int node_b = wires[i][1];
            visit[node_b] = true;
            Queue<Integer> queue_b = new LinkedList();
            queue_b.add(node_b);
            int cnt_b = 1;
            while(!queue_b.isEmpty()){
                int node = queue_b.poll();
                for (int nextNode: graph.get(node)){
                    if (!visit[nextNode]){
                        queue_b.add(nextNode);
                        cnt_b++;
                        visit[nextNode] = true;
                    }
                }
            }
            
            answer = Math.min(answer,Math.abs(cnt_a-cnt_b));
        }
        return answer;
    }
}