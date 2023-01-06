import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")


import heapq
from collections import defaultdict

# 목적지, 간선의 개수
n, e = map(int,input().split())

# 양방향 그래프 저장
graph = defaultdict(list)
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

# 경유지
v1, v2 = map(int,input().split())


# 다익스트라 알고리즘
def dijkstra(start):
    hq = [(0,start)]
    dis = [1e9] * (n+1)
    # 맨 처음 노드는 0으로 설정
    dis[start] = 0
    while hq:
        l, node = heapq.heappop(hq)
        for x in sorted(graph[node]):   
            nl, next_node = x
            # 최단거리로 이동해야 하므로 dis가 이미 더 작은 값이 들어가 있다면 이동 x
            if dis[next_node] > nl+l:
                dis[next_node] = nl+l
                heapq.heappush(hq,(nl+l,next_node))
    return dis

# 다익스트라는 한 정점에서 모든 정점까지의 최단거리를 갱신
one_ = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

case1 = one_[v1] + v1_[v2] + v2_[n]
case2 = one_[v2] + v2_[v1] + v1_[n]
ans = min(case1, case2)

# 방법이 없다면 -1출력
print(ans if ans < 1e9 else -1)