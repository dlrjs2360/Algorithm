class Solution {
    public int solution (int n, int[][] results){
        boolean[][] game =  new boolean[n][n];
        int answer = 0;
        for(int i=0; i<results.length; i++){ game[results[i][0]-1][results[i][1]-1]=true; }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                for(int k=0; k<n; k++){
                    if(game[j][i]&&game[i][k]){game[j][k]=true;}
                }
            }
        }

        for(int i=0; i<n; i++){
            int result=0;
            for(int j=0; j<n; j++){
                if(game[i][j] || game[j][i]){result++;}
            }
            if(result==n-1){answer++;}
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