import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Stack<Integer> stack = new Stack();
        
        int is;
        for (String s : number.split("")) {
            is = Integer.parseInt(s);
            
            while ( k > 0 && !stack.isEmpty()) {
                int sv = stack.pop();
                if (sv < is) { k --; } 
                else { stack.push(sv); break;}
            }
            
            stack.push(is);
        }
        
        while (k-- > 0) stack.pop();
        
        String answer = "";
        while (!stack.isEmpty()) {
            answer = String.valueOf(stack.pop()) + answer;
        }
        
        return answer;
    }
}