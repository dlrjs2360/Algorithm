import sys
input = sys.stdin.readline
from heapq import heappop,heappush

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
t = 1
while 1:
    N = int(input())
    if N == 0: break
    graph = [list(map(int, input().split())) for _ in range(N)]
    heap = []
    heappush(heap,(graph[0][0], 0, 0))
    dist = [[1e9] * N for _ in range(N)]
    while heap:
        w, x, y = heappop(heap)
        if (x == N - 1 and y == N - 1) or dist[x][y] < w: continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N) or dist[nx][ny] <= (nw := w + graph[nx][ny]): continue
            dist[nx][ny] = nw
            heappush(heap,(nw, nx, ny))
    print(f"Problem {t}: {dist[N - 1][N - 1]}")
    t += 1