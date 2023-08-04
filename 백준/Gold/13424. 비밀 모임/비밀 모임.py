import sys
input = sys.stdin.readline

MAX = int(1e9)

for _ in range(int(input())):
    N,M = map(int,input().split())
    graph = [[MAX] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        graph[a][b] = c
        graph[b][a] = c

    for x in range(1,N+1):
        graph[x][x] = 0    
        
    for k in range(1,N+1):
        for x in range(1,N+1):
            for y in range(1,N+1):
                graph[x][y] = min(graph[x][y],graph[x][k]+graph[k][y])

    K = int(input())
    frineds = list(map(int,input().split()))
    answer,prev = 0,1e9
    for n in range(1,N+1):
        S = sum(graph[x][n] for x in frineds)
        if S < prev:
            answer = n
            prev = S

    print(answer)