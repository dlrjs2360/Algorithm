import java.util.*;

class Solution {
    public String solution(int n) {
        String answer = "";
        List<String> arr = new ArrayList<>();
        int t;
        while (n > 0) {
            t = n % 3;
            if (t == 0) {
                arr.add("4");
                n--;
            }
            else {
                arr.add(String.valueOf(t));
            }
            n /= 3;
            
        }
        
        for (int i = arr.size()-1; i >= 0; i--) {
            answer += arr.get(i);
        }
        
        return answer;
    }
    
}