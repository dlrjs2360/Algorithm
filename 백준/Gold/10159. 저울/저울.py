import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
item = [list(map(int,input().split())) for _ in range(M)]
graph = [[0] * (N+1) for _ in range(N+1)]

for a,b in item:
    graph[a][b] = 1
    graph[b][a] = -1

for h in range(1,N+1):
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if graph[x][y] != 0: continue
            a,b = graph[x][h],graph[y][h]
            if a == 1 and b == -1:
                graph[x][y] = 1
                graph[y][x] = -1
            elif a == -1 and b == 1:
                graph[y][x] = 1
                graph[x][y] = -1

for i in range(1,N+1):
    print(graph[i].count(0)-2)