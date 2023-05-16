import sys
from collections import deque
input = sys.stdin.readline

def year():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                # spring
                if land[i][j] >= tree[i][j][k]:
                    land[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                    if tree[i][j][k]%5 == 0:
                        prod.append([i, j])
                # summer
                else:
                    for x in range(len(tree[i][j])-1, k-1, -1):
                        land[i][j] += tree[i][j][x] // 2
                        tree[i][j].pop()
                    break
    # fall
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    while prod:
        y, x = prod.pop()
        for i in range(8):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < n and 0 <= xx < n:
                tree[yy][xx].appendleft(1)
    # winter
    for i in range(n):
        for j in range(n):
            land[i][j] += arr[i][j]

n, m, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
land = [[5 for _ in range(n)] for _ in range(n)]
tree = [[deque([]) for _ in range(n)] for _ in range(n)]
prod = []
answer = 0

for i in range(m):
    x, y, z = map(int,input().split())
    tree[x-1][y-1].append(z)
for i in range(k):
    year()
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)