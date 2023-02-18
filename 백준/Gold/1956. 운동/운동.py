import sys
input = sys.stdin.readline

v,e = map(int,input().split())
dist = [[1e9]*(v+1) for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    dist[a][b] = c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
answer = 1e9
for i in range(1,v+1):
    answer = min(answer,dist[i][i])

print(answer if answer < 1e9 else -1)