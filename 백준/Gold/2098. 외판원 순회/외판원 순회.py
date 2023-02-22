import sys
input = sys.stdin.readline

def DFS(node,visited):
    if visited == (1 << (n-1)) - 1:
        if distance[node][0]:
            return distance[node][0]
        return INF

    if dp[node][visited] != 0:
        return dp[node][visited]
    dis = INF
    for i in range(1,n):
        if not distance[node][i] or visited & (1 << (i-1)):
            continue
        dis = min(dis, distance[node][i] + DFS(i, visited | (1 << (i-1))))
    dp[node][visited] = dis
    return dp[node][visited]

n = int(input())
INF = float('inf')
distance = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]
print(DFS(0,0))