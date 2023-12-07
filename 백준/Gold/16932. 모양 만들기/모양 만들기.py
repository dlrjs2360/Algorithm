N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

island = [[0] * M for _ in range(N)]
islandNum = 1

islandCnt = [0] * 1000001

dx,dy = [1,0,0,-1],[0,1,-1,0]
visit = [[False] * M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0 or visit[x][y]: continue
        island[x][y] = islandNum
        stack = [(x, y)]
        visit[x][y] = True
        cnt = 1
        while stack:
            a,b = stack.pop()
            for i in range(4):
                na, nb = a+dx[i], b+dy[i]
                if 0 <= na < N and 0 <= nb < M and graph[na][nb] == 1 and not visit[na][nb]:
                    visit[na][nb] = True
                    island[na][nb] = islandNum
                    stack.append((na,nb))
                    cnt += 1
        islandCnt[islandNum] = cnt
        islandNum += 1

answer = 0
for x in range(N):
    for y in range(M):
        if visit[x][y]: continue
        visit2 = []
        res = 1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and island[nx][ny] not in visit2:
                visit2.append(island[nx][ny])
                res += islandCnt[island[nx][ny]]

        answer = max(answer,res)
    
print(answer)