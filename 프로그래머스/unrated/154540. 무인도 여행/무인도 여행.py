from collections import deque

def solution(maps):
    
    answer = []
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    lx,ly = len(maps),len(maps[0])
    visit = [[False] * ly for _ in range(lx)]
    
    for i in range(lx):
        for j in range(ly):
            if visit[i][j] or maps[i][j] == "X":
                continue    
            Q = deque([(i,j)])
            total = int(maps[i][j])
            visit[i][j] = True
            while Q:
                x,y = Q.popleft()
                for h in range(4):
                    nx,ny = x+dx[h], y+dy[h]
                    if (not 0 <= nx < lx) or (not 0 <= ny < ly):
                        continue
                    if visit[nx][ny] or maps[nx][ny] == "X":
                        continue
                    Q.append((nx,ny))
                    total += int(maps[nx][ny])
                    visit[nx][ny] = True
                    
            answer.append(total)
                
    return sorted(answer) if answer else [-1]