// 나올 수 없는 상황
// 1. X 개수가 O 개수를 넘기는 상황
// 2. O가 정답을 맞췄는데 X와 O의 개수가 같은 상황
// 3. X가 정답을 맞췄는데 O가 X보다 많은 상황
// 4. O와 X의 개수가 2개 이상 차이나는 상황
// 5. 

import java.util.*;

class Solution {
    public int solution(String[] board) {
        int oc = 0, xc = 0;
        char c;
        boolean os = false, xs = false;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                c = getChar(board[i],j);
                if (c == 'O') {
                    oc += 1;
                } else if (c == 'X') {
                    xc += 1;
                }
                
                if (c == '.') { continue; }
                
                if (i == 0 && j == 0 && getChar(board[1],1) == c && getChar(board[2],2) == c) { // 좌우대각선
                    os = ((os || c == 'O') ? true : false);
                    xs = ((xs || c == 'X') ? true : false);
                }
                if (i == 0 && getChar(board[1],j) == c && getChar(board[2],j) == c) { // 세로
                    os = ((os || c == 'O') ? true : false);
                    xs = ((xs || c == 'X') ? true : false);
                }
                if (j == 0 && getChar(board[i],1) == c && getChar(board[i],2) == c) { // 가로
                    os = ((os || c == 'O') ? true : false);
                    xs = ((xs || c == 'X') ? true : false);
                }
                if (i == 0 && j == 2 && getChar(board[1],1) == c && getChar(board[2],0) == c) { // 우좌대각선
                    os = ((os || c == 'O') ? true : false);
                    xs = ((xs || c == 'X') ? true : false);
                }
                
            }
        }
        
        System.out.println(os + " " + xs + " " + oc + " " + xc);
        
        if ( (xc > oc) || (oc > xc+1) || (os && (xc >= oc)) || (xs && (oc > xc)) || (os && xs && (xc >= oc))) { return 0; }
        
        return 1;
    }
    
    char getChar(String s, int i) {
        return s.charAt(i);
    }

}