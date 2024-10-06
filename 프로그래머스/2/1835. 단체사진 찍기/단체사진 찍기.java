

class Solution {
    String[] d ;
    int answer = 0;
    public int solution(int n, String[] data) {
        d=data;
        dfs("");
        return answer;
    }
    void dfs(String s){
        if(s.length() != 8){
            if(s.indexOf("A") == -1) dfs(s+"A");
            if(s.indexOf("C") == -1) dfs(s+"C");
            if(s.indexOf("F") == -1) dfs(s+"F");
            if(s.indexOf("J") == -1) dfs(s+"J");
            if(s.indexOf("M") == -1) dfs(s+"M");
            if(s.indexOf("N") == -1) dfs(s+"N");
            if(s.indexOf("R") == -1) dfs(s+"R");
            if(s.indexOf("T") == -1) dfs(s+"T");
        }
        else{
            boolean flag = true;
            for(int i = 0 ; i<d.length; i++){
                char p1 = d[i].charAt(0);
                char p2 = d[i].charAt(2);
                int btwNum = Math.abs(s.indexOf(p1)-s.indexOf(p2))-1;
                char c = d[i].charAt(3);
                int cndNum = d[i].charAt(4)-'0';
                if(c == '='){
                    if(btwNum != cndNum){
                        flag = false;
                        break;
                    }
                }
                else if( c== '>'){
                    if(btwNum<=cndNum){
                        flag = false;
                        break;
                    }
                }
                else{
                    if(btwNum>=cndNum){
                        flag = false;
                        break;
                    }
                }
            }
            if(flag) answer++;
        }
    }
}