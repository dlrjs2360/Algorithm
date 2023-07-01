import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def ancestor(node):
    if parent[node] != node: parent[node] = ancestor(parent[node])
    return parent[node]

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(i+1,n):
        heappush(heap,(graph[i][j],i,j))

answer = 0
parent = [i for i in range(n)]
while heap:
    w,x,y = heappop(heap)
    ax,ay = ancestor(x), ancestor(y)
    if ax == ay: continue
    if ax < ay : ax,ay = ay,ax
    parent[ay] = ax
    answer += w

print(answer)