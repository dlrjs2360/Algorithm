class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0,1000001};
        int end = 0;
        int total = 0;
        for (int i = 0; i < sequence.length; i++){
            while (total < k && end < sequence.length){
                total += sequence[end];
                end++;
            }
            if ( total == k && (end-i-1) < (answer[1]-answer[0]) ){
                answer[0] = i;
                answer[1] = end-1;
            }
            total -= sequence[i];
        };
        
        return answer;
    }
}