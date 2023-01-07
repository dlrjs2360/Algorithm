import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

n = int(input())
arr = [list(input()) for _ in range(n)]

# 방문처리
visit_weakness = [[False] * (n+1) for _ in range(n)]
visit_common = [[False] * (n+1) for _ in range(n)]

# 구역처리
check_weakness = {"R" : ["R", "G"], "G" : ["R", "G"], "B":["B"]}
check_common = {"R" : ["R"], "G" : ["G"], "B":["B"]}

# 방향처리
dx = [-1,0,0,1]
dy = [0,1,-1,0]

# 깊이우선탐색
def DFS(visit, x, y, check):
    if visit[x][y] or arr[x][y] not in check:
        return visit
    visit[x][y] = True
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < n and 0 <= next_y < n and not visit[next_x][next_y]:
            visit = DFS(visit,next_x,next_y,check)
    return visit

# 그래프탐색
ans_common, ans_weakness = 0, 0
for x in range(n):
    for y in range(n):
        if not visit_common[x][y]:
            visit_common = DFS(visit_common, x, y, check_common[arr[x][y]])
            ans_common += 1
        if not visit_weakness[x][y]:
            visit_weakness = DFS(visit_weakness, x, y, check_weakness[arr[x][y]])
            ans_weakness += 1

print(ans_common, ans_weakness)

