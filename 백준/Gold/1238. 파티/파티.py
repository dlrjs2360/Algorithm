import sys
input = sys.stdin.readline

import heapq
def dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    dist = [1e9] * (n + 1)
    dist[start] = 0
    while Q:
        total, node = heapq.heappop(Q)
        if dist[node] < total:
            continue
        for time,next_node in edges[node]:
            s = total + time
            if dist[next_node] > s:
                dist[next_node] = s
                heapq.heappush(Q,(s,next_node))
    return dist


n,m,x = map(int,input().split())
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,t = map(int,input().split())
    edges[a].append([t,b])

ans = 0
back = dijkstra(x)
for i in range(1,n+1):
    go = dijkstra(i)
    ans = max(back[i] + go[x], ans)

print(ans)

