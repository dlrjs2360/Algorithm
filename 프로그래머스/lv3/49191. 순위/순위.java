import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;

        Map<Integer, Set<Integer>> win = new HashMap<>();
        Map<Integer, Set<Integer>> lose = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            win.put(i, new HashSet<>());
            lose.put(i, new HashSet<>());
        }

        for (int[] result : results) {
            lose.get(result[1]).add(result[0]);
            win.get(result[0]).add(result[1]);
        }

        for (int i = 1; i <= n; i++) {
            for (int winner : lose.get(i)) {
                win.get(winner).addAll(win.get(i));
            }

            for (int loser : win.get(i)) {
                lose.get(loser).addAll(lose.get(i));
            }
        }

        for (int i = 1; i <= n; i++) {
            if (win.get(i).size() + lose.get(i).size() == n - 1) {
                answer++;
            }
        }

        return answer;
    }
}
/*
나를 이긴 사람의 수 + 나에게 진 사람의 수 = 전체 - 1
import java.util.*;

    public int solution(int n, int[][] results) {
        
        int answer = 0;
        
        HashMap<Integer,Set<Integer>> winning = new HashMap<>();
        for (int i = 1; i <= n; i++) winning.put(i,new HashSet<Integer>());
        HashMap<Integer,Set<Integer>> losing = new HashMap<>();
        for (int i = 1; i <= n; i++) losing.put(i,new HashSet<Integer>());
        
        for (int[] r : results){
            winning.get(r[0]).add(r[1]); // 나에게 진 사람
            losing.get(r[1]).add(r[0]); // 나에게 이긴 사람
        }
        System.out.println("원본");
        System.out.println("이긴사람들: "+winning.toString());
        System.out.println("진사람들: "+losing.toString());
        
        for (int i = 1; i <= n; i++){
            for (int winner_to_me: losing.get(i)) losing.get(winner_to_me).addAll(winning.get(i));
            for (int loser_to_me: winning.get(i)) winning.get(loser_to_me).addAll(losing.get(i));
        } 
        
        for (int i=1; i <= n; i++){
            if (winning.get(i).contains(i)) winning.get(i).remove(i);
            if (losing.get(i).contains(i)) losing.get(i).remove(i);
            if (winning.get(i).size() + losing.get(i).size() == n-1) answer ++;
        }
        System.out.println("결과");
        System.out.println("이긴사람들: "+winning.toString());
        System.out.println("진사람들: "+losing.toString());
        
        return answer;
    }
}
*/