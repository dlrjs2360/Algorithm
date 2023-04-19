from collections import deque

def BFS(start,end,maps):
    q = deque([(0,start[0],start[1])])
    lx,ly = len(maps),len(maps[0])
    visit = [[False] * ly for _ in range(lx)]
    visit[start[0]][start[1]] = True
    while q:
        cnt,x,y = q.popleft()
        if x == end[0] and y == end[1]:
            return cnt
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0 <= nx < lx and 0 <= ny < ly and maps[nx][ny] != 'X' and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((cnt+1,nx,ny))
    return 1e9
                
def solution(maps):
    answer = 0
    start, end, lever = [],[],[]
    for i in range(lx:=len(maps)):
        for j in range(ly:=len(maps[0])):
            v = maps[i][j]
            if v == 'S':
                start = [i,j]
            if v == 'E':
                end = [i,j]
            if v == 'L':
                lever = [i,j]
    answer += BFS(start,lever,maps) + BFS(lever,end,maps)
    return answer if answer < 1e9 else -1