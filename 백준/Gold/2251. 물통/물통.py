A, B, C = map(int, input().split())
answer = set()
visit = [[[False] * (C + 1)] * (B + 1) for _ in range(A + 1)]

def DFS(a, b, c):
    global answer
    if visit[a][b][c]: return
    visit[a][b][c] = True
    if a == 0:
        answer.add(c)
    if b > 0:
        DFS(min(b + a, A), max(0, b - (A-a)), c)
        DFS(a, max(0, b - (C-c)), min(C, c + b))
    if c > 0:
        DFS(min(c + a, A), b, max(0, c - (A-a)))
        DFS(a, min(b + c, B), max(0, c - (B-b)))
    if a > 0:
        DFS(max(0, a - (C-c)), b, min(C, c + a))
        DFS(max(0, a - (B-b)), min(b + a, B), c)

DFS(0, 0, C)

print(*sorted(answer))