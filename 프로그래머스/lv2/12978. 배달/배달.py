from heapq import heappop,heappush
from collections import defaultdict

def dijkstra(start,N,road,graph):
    dist = [1e9] * (N+1)
    dist[start] = 0
    heap = [(0,start)]
    while heap:
        d,node = heappop(heap)
        for c,nnode in sorted(graph[node]):
            if dist[nnode] > d+c:
                dist[nnode] = d+c
                heappush(heap,(d+c,nnode))
    return dist

def solution(N, road, K):
    graph = defaultdict(list)
    for a,b,c in road:
        graph[a].append((c,b))
        graph[b].append((c,a))
    dist = dijkstra(1,N,road,graph)
    return sum([1 for x in dist if x <= K ])