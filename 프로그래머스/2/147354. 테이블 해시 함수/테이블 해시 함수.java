import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        Arrays.sort(data, (a,b) -> {
            if (a[col-1] != b[col-1]) {
                return Integer.compare(a[col-1], b[col-1]);
            }
            return Integer.compare(-a[0], -b[0]);
        });
        
        for (int i = row_begin; i <= row_end; i++) {
            final int num = i;
            answer ^= Arrays.stream(data[i-1])
                .map((a) -> {return a % num;})
                .sum();
            //System.out.println(answer);
        }
        
        return answer;
    }
}