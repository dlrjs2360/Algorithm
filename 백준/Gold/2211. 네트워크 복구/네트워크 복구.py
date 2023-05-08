import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappop,heappush

n,m = map(int,input().split())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

answer = []

dist = [1e9] * (n+1)
dist[1] = 0
link = [x for x in range(n+1)]
heap = [[0,1]]
while heap:
    nw, node = heappop(heap)
    for w, nextNode in sorted(graph[node]):
        if dist[nextNode] > w+nw:
            dist[nextNode] = w+nw
            link[nextNode] = node
            heappush(heap,[w+nw,nextNode])
print(n-1)
for i,x in enumerate(link):
    if i < 2:
        continue
    print(i,x)
