import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
graph = [list(input()) for _ in range(N)]
target = [list(map(int, input().split())) for _ in range(K)]

gj = [[0] * (M+1) for _ in range(N+1)]
go = [[0] * (M+1) for _ in range(N+1)]
gi = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    J, O, I = 0, 0, 0
    for j in range(1,M+1):
        if graph[i-1][j-1] == "J": J += 1
        elif graph[i-1][j-1] == "O": O += 1
        else: I += 1
        gj[i][j] = J
        go[i][j] = O
        gi[i][j] = I

for j in range(1,M+1):
    for i in range(1,N+1):
        gj[i][j] += gj[i - 1][j]
        go[i][j] += go[i - 1][j]
        gi[i][j] += gi[i - 1][j]

for a, b, c, d in target:
    aj = gj[c][d] - gj[a-1][d] - gj[c][b-1] + gj[a-1][b-1]
    ao = go[c][d] - go[a-1][d] - go[c][b-1] + go[a-1][b-1]
    ai = gi[c][d] - gi[a-1][d] - gi[c][b-1] + gi[a-1][b-1]
    print(aj,ao,ai)