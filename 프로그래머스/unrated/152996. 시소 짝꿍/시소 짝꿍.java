import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.Map;
import java.util.HashMap;

class Solution {
    private boolean canEqual(int a, int b) {
        return a * 3 == b * 2
            || a * 4 == b * 2
            || a * 4 == b * 3;
    }


    public long solution(int[] weights) {
        long answer = 0;
        Map<Integer, Long> players = Arrays.stream(weights)
                                           .boxed()
                                           .collect(Collectors.groupingBy(Integer::intValue, Collectors.counting()));
        for(Integer playerA : players.keySet()) {
            if(players.get(playerA) > 1) {
                answer += players.get(playerA) * (players.get(playerA) - 1) / 2;
            }
            for(Integer playerB : players.keySet()) {
                if(playerA < playerB && canEqual(playerA, playerB)) {
                    answer += players.get(playerA) * players.get(playerB);
                }
            }
        }
        return answer;
    }
}