
def dfs(cnt, x, y, pt):
    global answer

    if cnt >= N:
        answer += pt
        return

    for p, way in direction:
        if p == 0 : continue
        nx,ny = x + way[0], y + way[1]
        if visit[nx][ny]: continue
        visit[nx][ny] = True
        dfs(cnt + 1, nx, ny, pt*(p/100))
        visit[nx][ny] = False

N, *percent = map(int,input().split())

direction = list(zip(percent,[(0,1),(0,-1),(1,0),(-1,0)]))
visit = [[False] * (4*N) for _ in range(4*N)]

visit[2*N][2*N] = True

answer = 0
dfs(0,2*N,2*N,1)

print(answer)
