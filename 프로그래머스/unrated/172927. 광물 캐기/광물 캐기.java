import java.util.*;

class Solution {
    
    int answer = Integer.MAX_VALUE;
    public int solution(int[] picks, String[] minerals) {
        HashMap<String,Integer> toolNum = new HashMap();
        toolNum.put("diamond",0);
        toolNum.put("iron",1);
        toolNum.put("stone",2);
        int[][] score = {{1,1,1},{5,1,1},{25,5,1}};
        for (int p=0;p<3;p++){
            if (picks[p] <= 0){ // 해당 곡괭이가 부족한 경우
                continue;
            }
            picks[p]--;
            dfs(picks,minerals,toolNum,score,0,0,p);
            picks[p]++;
        }
        return answer;
    }
    
    public void dfs(int[] picks, String[] minerals, HashMap<String,Integer> toolNum, int[][] score, int total, int idx, int pick){
        int cnt = 0;
        while (cnt < 5 && idx < minerals.length){ // 곡괭이로 5개까지 캐기
            total += score[pick][toolNum.get(minerals[idx])];
            idx++;
            cnt++;
        }
        //System.out.println("total: "+total+" pick: "+pick+" picks: "+Arrays.toString(picks));
        if (cnt < 5 || idx >= minerals.length){ // 캘 광물이 없는 경우
            answer = Math.min(answer,total);
            return;
        }
        if (Arrays.stream(picks).sum() == 0){ // 모든 곡괭이를 다 사용한 경우
            answer = Math.min(answer,total);
            return;
        }
        for (int p=0;p<3;p++){
            if (picks[p] <= 0){ // 해당 곡괭이가 부족한 경우
                continue;
            }
            picks[p]--;
            dfs(picks,minerals,toolNum,score,total,idx,p);
            picks[p]++;
        }
    }
}