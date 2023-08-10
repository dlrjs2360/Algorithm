import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
parent = [[-1 for _ in range(M)] for _ in range(N)]

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(x, y, idx):
    global answer
    if parent[x][y] != -1:
        if parent[x][y] == idx: answer += 1
        return
    parent[x][y] = idx
    d = direction.index(graph[x][y])
    move(x + dx[d], y + dy[d], idx)

idx, answer = 0, 0
for i in range(N):
    for j in range(M):
        move(i, j, idx)
        idx += 1

print(answer)