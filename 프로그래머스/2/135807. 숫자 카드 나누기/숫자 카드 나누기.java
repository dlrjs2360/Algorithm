import java.util.*;

// 각 배열의 최소값을 찾는다.
// 최소값의 약수 중 각 배열을 모두 나눌 수 있는지 체크한다.
// 모두 나눌 수 있는 값들로 상대 배열을 모두 나눌 수 없는지 체크한다.

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        
        int cpa = getCp(arrayA);
        int cpb = getCp(arrayB);
        
        System.out.println(cpa + " " + cpb);
        
        boolean status = false;
        if(cpa > 0) {
            status =  Arrays.stream(arrayB).allMatch(v -> v % cpa != 0);
            if (status) { answer = cpa; }
        }
        
        if(cpb > 0) {
            status =  Arrays.stream(arrayA).allMatch(v -> (v % cpb != 0));
            if (status) { answer = Math.max(answer,cpb); }
        }
        
        return answer;
    }
    
    int getCp(int[] arr) {
        List<Integer> tmp = new ArrayList();
        int minVal = Arrays.stream(arr).min().getAsInt();
        for (int i = 1; i <= Math.sqrt(minVal)+1; i++) {
            if (minVal % i == 0) {
                if (i > 1) {
                    tmp.add(i);    
                }
                tmp.add(minVal / i);
            }
        }
        
        OptionalInt oi = tmp.stream().filter(t -> Arrays.stream(arr).allMatch(v -> (v % t == 0)))
                            .mapToInt(Integer::intValue).max();
        
        if (oi.isPresent()) { return oi.getAsInt(); }
        return -1;
    }
    
}