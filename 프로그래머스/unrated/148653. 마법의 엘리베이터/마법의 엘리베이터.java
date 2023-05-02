class Solution {
    public int solution(int storey) {
        return storey < 10 ? Math.min(storey, 11 - storey) : Math.min(storey % 10 + solution(storey / 10), 10 - storey % 10 + solution(storey / 10 + 1));
    }
}
