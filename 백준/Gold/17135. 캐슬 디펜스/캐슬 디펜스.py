from collections import deque
from itertools import combinations

n,m,dist = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def attack(archor):
    field = [x[:] for x in graph]
    killed = [[0] * m for _ in range(n)]
    result = 0
    for i in range(n - 1, -1, -1):
        killedNow = []
        for ay in archor:
            dq = deque([(i, ay, 1)])
            while dq:
                x, y, d = dq.popleft()
                if field[x][y] == 1:
                    killedNow.append((x, y))
                    if killed[x][y] == 0:
                        killed[x][y] = 1
                        result += 1
                    break
                if d < dist:
                    for nx,ny in [(x+dx[di],y+dy[di]) for di in range(3) if 0 <= x+dx[di] < n and 0 <= y+dy[di] < m]:
                            dq.append((nx, ny, d + 1))
        # 한 턴에 공격한 애들 한번에 죽이기
        for x, y in killedNow:
            field[x][y] = 0
    return result

answer = 0
dx,dy = [0, -1, 0], [-1, 0, 1]
for archers in combinations(range(m),3):
    answer = max(answer,attack(archers))
print(answer)