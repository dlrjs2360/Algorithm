import java.util.*;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String,Integer> score = new HashMap<>();
        for (int i=0;i < name.length; i++){
            score.put(name[i],yearning[i]);
        }
        int idx = 0;
        for (String[] p: photo){
            int res = 0;
            for (String n:p){
                if (score.containsKey(n)){
                    res += score.get(n);
                }
            }
            answer[idx] = res;
            idx++;
        }
        return answer;
    }
}