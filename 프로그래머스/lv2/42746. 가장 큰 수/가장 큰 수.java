import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Integer[] num = Arrays.stream(numbers).boxed().toArray(Integer[]::new);

        Arrays.sort(num, new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b){
                String sb = (b+"").repeat(4).substring(0,4);
                String sa = (a+"").repeat(4).substring(0,4);
                return Integer.parseInt(sb) - Integer.parseInt(sa);
            }
        });

        for (int number: num){
            answer += number+"";
        }
        if (answer.charAt(0) == '0') return "0";
        return answer;
    }
}