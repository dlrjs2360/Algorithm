import sys
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
A,B,C = map(int,input().split())
M = int(input())

road = defaultdict(list)
for D,E,L in [list(map(int,input().split())) for _ in range(M)]:
    road[D].append((L,E))
    road[E].append((L,D))

dists = []
for friend in [A,B,C]:
    dist = [1e9] * (N+1)
    dist[friend] = 0
    heap = []
    heappush(heap,(0,friend))
    while heap:
        d,loc = heappop(heap)
        if d > dist[loc]: continue
        for nd,nextLoc in sorted(road[loc]):
            if dist[nextLoc] <= d+nd: continue
            dist[nextLoc] = d+nd
            heappush(heap,(nd+d,nextLoc))
    dists.append(dist)

answer = 0
maxDist = 0
for i in range(1,N+1):
    if i == A or i == B or i == C: continue
    result = min([dists[j][i] for j in range(3)])
    if result > maxDist:
        answer = i
        maxDist = result

print(answer)