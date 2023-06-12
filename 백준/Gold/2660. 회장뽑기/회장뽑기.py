n = int(input())
graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0
    
while 1:
    a,b = map(int,input().split())
    if a == b == -1: break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])

MAX = 1e9
answer = []
for i,x in enumerate(graph[1:]):
    max_v = max(x[1:])
    if max_v > MAX: continue
    if max_v < MAX:
        MAX = max_v
        answer = []
    answer.append(i+1)

print(MAX,len(answer))
print(*sorted(answer))
