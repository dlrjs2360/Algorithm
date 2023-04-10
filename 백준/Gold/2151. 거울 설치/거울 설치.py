from heapq import heappop,heappush
n = int(input())
arr = [list(input()) for _ in range(n)]
door = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "#":
            door.append((i,j))

dx,dy = [1,-1,0,0],[0,0,1,-1]

start = door.pop()
target = door.pop()

q = [(0,start[0],start[1])]
dis = [[1e9] * n for _ in range(n)]
while q:
    cnt,a,b = heappop(q)
    dis[a][b] = cnt
    if a == target[0] and b == target[1]:
        print(cnt-1)
        break
    for i in range(4):
        nx,ny = a,b
        while 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == "*":
                break
            elif arr[nx][ny] in ("!","#") and  dis[nx][ny] > cnt:
                dis[nx][ny] = cnt+1
                heappush(q,(cnt+1,nx,ny))
            nx += dx[i]
            ny += dy[i]