import java.util.*;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        List<Integer> answer = new ArrayList();
        HashMap<Character,Integer> numMap = new HashMap();
        
        for (String key: keymap){
            for (int i=0; i<key.length(); i++){
                Character word = key.charAt(i);
                if ((numMap.containsKey(word) && numMap.get(word) > i+1) || !numMap.containsKey(word)){
                    numMap.put(word,i+1);
                }
            }
        }
        
        for (String target: targets){
            int res = 0;
            for (int i=0; i < target.length(); i++){
                if (!numMap.containsKey(target.charAt(i))){
                    res = -1;
                    break;
                }
                res += numMap.get(target.charAt(i));
            }
            answer.add(res);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}