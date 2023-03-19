import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        jump = int(graph[x][y])
        mx, my = x + dx[i] * jump, y + dy[i] * jump
        if 0 <= mx < n and 0 <= my < m and graph[mx][my] != "H" and cnt+1 > dp[mx][my]:
            if visited[x] & (1 << y):
                print(-1)
                exit()
            dp[mx][my] = cnt + 1
            visited[x] |= (1 << y)
            DFS(mx,my,cnt+1)
            visited[x] ^= (1 << y)

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
ans = 0
visited = [0] * n
DFS(0,0,0)
print(ans+1)