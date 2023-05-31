import sys
input = sys.stdin.readline

from collections import deque

def BFS():
    while queue:
        if graph[D[0]][D[1]] == 'S':
            return dist[D[0]][D[1]]
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] in ('.','D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] in ('.','S') and graph[x][y] == "*":
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))
    return 'KAKTUS'

r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]

dx,dy = [1,0,0,-1],[0,1,-1,0]
D = []
queue = deque()
dist = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S': queue.append((i,j))
        elif graph[i][j] == 'D': D = [i,j]

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*': queue.append((i,j))

print(BFS())