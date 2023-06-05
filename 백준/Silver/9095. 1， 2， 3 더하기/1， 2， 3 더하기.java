import java.util.Scanner;

public class Main {
    public static int DFS(int target, int S, int answer) {
        if (target <= S) {
            if (target == S) {
                return 1;
            }
            return 0;
        } else {
            int temp = 0;
            for (int i = 1; i <= 3; i++) {
                temp += DFS(target, S + i, answer);
            }
            return temp;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int test_case = 0; test_case < T; test_case++) {
            System.out.println(DFS(scanner.nextInt(), 0, 0));
        }
    }
}