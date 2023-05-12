from collections import defaultdict,deque
from heapq import heappop,heappush
n = int(input())
MAX = float('inf')
graph = defaultdict(list)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

root = 1
parent = [x for x in range(n+1)]
dist = [MAX] * (n+1)
dist[root] = 0
depth = [0] * (n+1)
heap = [(0,root)]
while heap:
    w,node = heappop(heap)
    for nw,nextNode in graph[node]:
        if dist[nextNode] > w+nw:
            depth[nextNode] = depth[node]+1
            dist[nextNode] = w+nw
            heappush(heap,(w+nw,nextNode))
            parent[nextNode] = node

def LCS(a,b):
    while (da := depth[a]) != (db:=depth[b]):
        if da > db:
            a = parent[a]
            continue
        b = parent[b]
    while a != b:
        a,b = parent[a],parent[b]
    return a

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    lcs = LCS(a,b)
    print(dist[a]+dist[b]-2*dist[lcs])