import java.util.*;

class Solution {
    
    static boolean[] visit;
    static List<String> answer;
    
    public String[] solution(String[][] tickets) {
        answer = new ArrayList<>();
        visit = new boolean[tickets.length];
        
        dfs("ICN","ICN",0,tickets);
        
        Collections.sort(answer);
        return answer.get(0).split(" ");
    }
    
    static void dfs(String start, String res, int count, String[][] tickets) {
        if (count == tickets.length){
            answer.add(res);
            return;
        }
        for (int i = 0; i < tickets.length; i++){
            if (visit[i] || !start.equals(tickets[i][0])) continue;
            visit[i] = true;
            dfs(tickets[i][1], res+" "+tickets[i][1], count+1, tickets);
            visit[i] = false;
        }
    }
}