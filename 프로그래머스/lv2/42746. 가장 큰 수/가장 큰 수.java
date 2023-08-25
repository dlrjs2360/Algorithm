import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Integer[] num = Arrays.stream(numbers).boxed().toArray(Integer[]::new);

        Arrays.sort(num, (a,b) -> {
            return Integer.parseInt((b+"")+(a+"")) - Integer.parseInt((a+"") + (b+""));
        });

        for (int number: num){
            answer += number+"";
        }
        if (answer.charAt(0) == '0') return "0";
        return answer;
    }
}