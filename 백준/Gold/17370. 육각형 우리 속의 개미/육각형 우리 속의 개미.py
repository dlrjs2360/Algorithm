def bt(x,y,w,cnt):
    global answer

    if cnt >= N: return

    for t in turn[w]:
        nw = way[t]
        nx,ny = x+nw[0], y+nw[1]
        if visit[nx][ny]:
            if cnt+1 == N:
                answer += 1
            continue

        visit[nx][ny] = True
        bt(nx, ny, t, cnt+1)
        visit[nx][ny] = False


N = int(input())

answer = 0
sx, sy = 22, 22

visit = [[False] * 45 for _ in range(45)]
visit[sx][sy] = True
visit[sx+1][sy] = True

way = {
    "N": [-1,0],
    "S": [1,0],
    "SW": [1,-1],
    "NW": [-1,-1],
    "SE": [1,1],
    "NE": [-1,1]
}

turn = {
    "N": ["NW","NE"],
    "S": ["SW","SE"],
    "SW": ["NW","S"],
    "NW": ["N","SW"],
    "SE": ["S","NE"],
    "NE": ["N","SE"]
}

bt(sx, sy, "N",0)
print(answer)