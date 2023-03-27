from collections import deque

n = int(input())
sx,sy = -1,-1
graph = []
eat_cnt = 0
fish_cnt = 0
size = 2
time = 0
dx,dy = [-1,0,0,1],[0,-1,1,0]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(n):
        if l[j] == 9:
            sx,sy = i,j
        elif l[j] > 0:
            fish_cnt += 1
    graph.append(l)
graph[sx][sy] = 0

def BFS(x,y):
    Q = deque([(x,y,0)])
    dist_list = []
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    min_dist = 1e9
    while Q:
        x,y,dist = Q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] <= size:
                    visit[nx][ny] = True
                    if 0 < graph[nx][ny] < size:
                        min_dist = dist
                        dist_list.append((dist+1,nx,ny))
                    if dist+1 <= min_dist:
                        Q.append((nx,ny,dist+1))
    return sorted(dist_list)[0] if dist_list else False

while fish_cnt:
    res = BFS(sx,sy)

    if not res:
        break

    sx,sy = res[1],res[2]
    graph[sx][sy] = 0

    time += res[0]

    eat_cnt += 1
    fish_cnt -= 1

    if size == eat_cnt:
        size += 1
        eat_cnt = 0

print(time)