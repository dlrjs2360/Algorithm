n,m = map(int,input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]
dp = [[str(x)]*(n+1) for x in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    dp[a][b] = b
    dp[b][a] = a

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
                dp[i][j] = dp[i][k]

for i in range(1,n+1):
    dp[i][i] = "-"

for x in dp[1:]:
    print(*x[1:])