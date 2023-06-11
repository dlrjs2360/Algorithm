import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop



from collections import defaultdict
from heapq import heappush, heappop


def solution(start,end,MAX):
    heap = [(0,start)]
    dist = [0] + [MAX] * (n-1)
    while heap:
        w, node = heappop(heap)
        if dist[node] < w or ward[node]: continue
        for nw, nextNode in edge[node]:
            if dist[nextNode] <= w + nw: continue
            dist[nextNode] = w + nw
            heappush(heap, (w + nw, nextNode))
    return dist[end] if dist[end] < MAX else -1


n, m = map(int, input().split())
ward = list(map(int, input().split()))
edge = defaultdict(list)
start,end,MAX = 0,n-1,1e10+1
for _ in range(m):
    a, b, t = map(int, input().split())
    edge[a].append((t, b))
    edge[b].append((t, a))
print(solution(start,end,MAX))