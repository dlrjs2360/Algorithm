import java.util.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        int pt = 0;
        String heard = replaceShop(m);
        for (String music: musicinfos){
            String[] info = music.split(",");
            int playTime = convertor(info[1]) - convertor(info[0]);
            String name = info[2];
            String part = replaceShop(info[3]);
            String origin = part.repeat(playTime / part.length()) + part.substring(0,playTime % part.length());
            if (origin.contains(heard) && (answer.equals("(None)") || pt < playTime)){
                answer = info[2];
                pt = playTime;
            }
        }
        return answer;
    }
    
    public int convertor(String time){
        return Arrays.stream(time.split(":"))
        .mapToInt(Integer::parseInt)
        .reduce((h, m) -> h * 60 + m)
        .orElse(0);
    }
    
    public String replaceShop(String music) {
        return music.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a");
    }
}