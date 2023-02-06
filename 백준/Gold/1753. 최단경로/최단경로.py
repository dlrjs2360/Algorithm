import heapq
from collections import defaultdict
def dijkstra(start):
    next = [(0,start)]
    dis = [1e9] * (n+1)
    dis[start] = 0
    while next:
        l, node = heapq.heappop(next)
        if l > dis[node]:
            continue
        for x in sorted(graph[node]):
            nl, next_node = x
            if l+nl < dis[next_node]:
                dis[next_node] = l+nl
                heapq.heappush(next,(l+nl,next_node))
    return dis

n, e = map(int, input().split())
k = int(input())
graph = defaultdict(list)
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

dis = dijkstra(k)
for i in range(1,n+1):
    if dis[i] != 1e9:
        print(dis[i])
        continue
    print("INF")