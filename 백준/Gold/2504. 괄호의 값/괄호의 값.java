
import java.io.*;
import java.util.*;

public class Main {

    static String[] arr;
    static Stack<String> stack;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        arr = br.readLine().split("");
        stack = new Stack<>();
        int answer = 0;
        int tmp = 1;

        A:
        for (int i = 0; i < arr.length; i++) {
            String s = arr[i];
            switch (s) {
                case "(" :
                    tmp *= 2;
                    stack.push(s);
                    break;
                case "[" :
                    tmp *= 3;
                    stack.push(s);
                    break;
                case ")" :
                    if (i > 0 && arr[i-1].equals("(")) {
                        answer += tmp;
                        tmp /= 2;
                        stack.pop();
                        break;
                    } else if (!stack.empty() && stack.peek().equals("(")) {
                        tmp /= 2;
                        stack.pop();
                        break;
                    }
                    answer = 0;
                    break A;
                case "]" :
                    if (i > 0 && arr[i-1].equals("[")) {
                        answer += tmp;
                        tmp /= 3;
                        stack.pop();
                        break;
                    } else if (!stack.empty() && stack.peek().equals("[")) {
                        tmp /= 3;
                        stack.pop();
                        break;
                    }
                    answer = 0;
                    break A;
            }
        }

        if (!stack.empty()) answer = 0;

        System.out.println(answer);
    }
}