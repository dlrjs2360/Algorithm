import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x == N - 1 and y == M - 1: return 1
    if dp[x][y] != -1: return dp[x][y]
    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] >= graph[x][y]: continue
        ways += dfs(nx, ny)
    dp[x][y] = ways
    return dp[x][y]


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
dp = [[-1] * M for _ in range(N)]
print(dfs(0, 0))