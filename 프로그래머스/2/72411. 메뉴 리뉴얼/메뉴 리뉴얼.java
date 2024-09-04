// 이전에 각 손님들이 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
// 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
// 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 후보에 포함

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    
    static HashMap<String, Integer> count = new HashMap<>();
    
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        
        for (String o: orders) {
            String[] sep = o.split("");
            for (int c: course) {
                getComb(sep, c, new String(""), 0);
            }
        }
        
        for (int c: course) {
            int maxCount = 0;
            List<String> res = new ArrayList<>();
            for (Map.Entry<String, Integer> entry: count.entrySet()) {
                String key = entry.getKey();
                Integer val = entry.getValue();
                
                if (key.length() != c) { continue; }
                
                if (maxCount == val) {
                    res.add(key);
                } else if (val > maxCount) {
                    res.clear();
                    res.add(key);
                    maxCount = val;
                }
            }
            if (maxCount < 2) { continue; }
            answer.addAll(res);
        }
        
        
        return answer.stream().sorted().toArray(String[]::new);
    }
    
    void getComb(String[] sep, int c, String tmp, int start) {
        if (c == 0) {
            String res = Arrays.stream(tmp.split("")).sorted().collect(Collectors.joining(""));
            count.put(res,count.getOrDefault(res,0)+1);
            return;
        }
        
        for (int i = start; i < sep.length; i++) {
            getComb(sep, c-1, tmp+sep[i], i+1);
        }
    }
    
}