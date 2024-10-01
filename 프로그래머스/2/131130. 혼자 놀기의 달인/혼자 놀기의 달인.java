import java.util.*;

class Solution {
    public int solution(int[] cards) {
        cards = Arrays.stream(cards).map(c -> {return c-1;}).toArray();
        boolean[] visit = new boolean[cards.length];
        int maxV1 = 0;
        int maxV2 = 0;
        
        Deque<Node> queue = new LinkedList<>();
        for (int c: cards) {
            queue.addLast(new Node(0, c));
        }
        
        while (!queue.isEmpty()) {
            Node node = queue.pollFirst();
            if (visit[node.num]) {
                if (node.count > maxV1) { 
                    maxV2 = maxV1;
                    maxV1 = node.count; 
                } 
                else if (node.count > maxV2) { maxV2 = node.count; }
                continue;
            }
            visit[node.num] = true;
            
            queue.addFirst(new Node(node.count+1, cards[node.num]));
        }
        
        return maxV1 * maxV2;
    }
    
    class Node {
        int count, num;
        
        Node(int count, int num) {
            this.count = count;
            this.num = num;
        }
    }
}