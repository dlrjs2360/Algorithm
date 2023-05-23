import sys, heapq
input = sys.stdin.readline

INF = -1000000000
n,m = map(int,input().split())
link = [[] for _ in range(n+1)]
visited = [-INF]*(n+1)
for _ in range(m):
    a,b,c = map(int,input().split())
    link[a].append((b,-c))
    link[b].append((a,-c))
start,end = map(int,input().split())

hq = [(INF,start)]
while hq:
    max_w,v = heapq.heappop(hq)
    if v == end:
        print(-max_w)
        break
    for toNode,weight in link[v]:
        if visited[toNode] <= weight:
            continue
        visited[toNode] = weight
        heapq.heappush(hq,(max(max_w,weight), toNode))