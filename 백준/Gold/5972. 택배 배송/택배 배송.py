from collections import defaultdict
from heapq import heappop,heappush
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
edges = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    edges[a].append((c,b))
    edges[b].append((c,a))

MAX = float('inf')
heap = []
dist = [MAX] * (n+1)
dist[1] = 0
heappush(heap,(0,1))
while heap:
    w,node = heappop(heap)
    if dist[node] < w: continue
    for nw, nn in sorted(edges[node]): # sorted에 대한 생각(위의 조건문과 연결)
        if dist[nn] <= w+nw : continue
        dist[nn] = w+nw
        heappush(heap,(dist[nn],nn))

print(dist[n])