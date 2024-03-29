def calc(n1, op, n2):
    if op == "+": return n1 + n2
    if op == "-": return n1 - n2
    if op == "*": return n1 * n2

def dfs(depth, v):
    global ans
    if depth == N - 1: ans = max(ans, v); return
    if depth + 2 < N:  dfs(depth + 2, calc(v, S[depth + 1], int(S[depth + 2])))
    if depth + 4 < N: dfs(depth + 4, calc(v, S[depth + 1], calc(int(S[depth + 2]), S[depth + 3], int(S[depth + 4]))))

N = int(input())
S = input()
ans = -1e9
dfs(0, int(S[0]))
print(ans)