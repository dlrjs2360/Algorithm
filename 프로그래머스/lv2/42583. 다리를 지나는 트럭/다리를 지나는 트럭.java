import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
          Queue<Integer> q = new LinkedList<>();
        int time = 0;
        int total_weight = 0;

        for (int i = 0; i < truck_weights.length; i++) {
            int truck_weight = truck_weights[i];

            while (true) {
                if (q.isEmpty()) {
                    q.add(truck_weight);
                    total_weight += truck_weight;
                    time++;
                    break;
                } else if (q.size() == bridge_length) {
                    total_weight -= q.poll();
                } else {
                    if (total_weight + truck_weight > weight) {
                        q.add(0);
                        time++;
                    } else {
                        q.add(truck_weight);
                        total_weight += truck_weight;
                        time++;
                        break;
                    }
                }
            }
        }
        return time + bridge_length;
    }
}