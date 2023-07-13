from collections import deque

def calc_bridge_size(a, b):
    global result
    for x1, y1 in islands[a]:
        for x2, y2 in islands[b]:
            result = min(result, (abs(y2 - y1) + abs(x2 - x1) - 1))
            if result == 1:
                return


def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 2
    island = [(x, y)]
    while queue:
        x, y = queue.popleft()
        for deltaX, deltaY in delta:
            X = x + deltaX
            Y = y + deltaY
            if 0 <= X < N and 0 <= Y < N and graph[X][Y] == 1:
                graph[X][Y] = 2
                queue.append((X, Y))
                island.append((X, Y))
    return island


delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
islands = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            islands.append(bfs(i, j))
result = 20000
for i in range(len(islands) - 1):
    for j in range(i + 1, len(islands)):
        calc_bridge_size(i, j)
        if result == 1:
            break
    if result == 1:
        break
print(result)