
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

from heapq import heappop, heappush

N,M = map(int,input().split())
graph = []
arr = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(M):
        if graph[i][j] == 1: arr.append((i,j))

H,W,Sr,Sc,Fr,Fc = map(int,input().split())

for x,y in arr:
    for i in range(H):
        if x - i < 0: break
        for j in range(W):
            if y - j < 0: break
            graph[x-i][y-j] = -1

heap = []
heappush(heap,(0,Sr-1,Sc-1))
dx,dy = [1,-1,0,0], [0,0,1,-1]
while heap:
    cnt, x,y = heappop(heap)
    if x == Fr-1 and y == Fc-1:
        print(cnt)
        break
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx > N-H or ny > M-W or graph[nx][ny] < 0: continue
        if graph[nx][ny] != 0 and graph[nx][ny] <= cnt+1: continue
        heappush(heap,(cnt+1,nx,ny))
        graph[nx][ny] = cnt+1
else:
    print(-1)