from collections import defaultdict
from heapq import heappop,heappush

n,m,r = map(int,input().split())
item = [0]+list(map(int,input().split()))

graph = defaultdict(list)
for _ in range(r):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

answer = 0
for start in range(1,n+1):
    heap = [start]
    dist = [1e9] * (n+1)
    dist[start] = 0
    while heap:
        node = heappop(heap)
        for w,nextNode in sorted(graph[node]):
            if dist[nextNode] > (nw := dist[node]+w):
                dist[nextNode] = nw
                heappush(heap,nextNode)
    answer = max(answer,sum([item[x] for x in range(1,n+1) if dist[x] <= m]))

print(answer)