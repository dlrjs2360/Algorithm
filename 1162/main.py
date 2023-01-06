import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

# 입력 받기
import heapq
from collections import defaultdict
INF = sys.maxsize
n, m, k = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijkstra(start):
    dis = [[INF] * (k+1) for _ in range(n+1)]
    dis[start][0] = 0
    Q = []
    heapq.heappush(Q,(0,start,0))
    while Q:
        l, node, cnt = heapq.heappop(Q)
        if dis[node][cnt] < l:
            continue
        for nl,next_node in graph[node]:
            next_l = nl+l
            if dis[next_node][cnt] > next_l:
                dis[next_node][cnt] = next_l
                heapq.heappush(Q, (next_l,next_node,cnt))
            if cnt < k and dis[next_node][cnt+1] > l:
                dis[next_node][cnt+1] = l
                heapq.heappush(Q, (l, next_node, cnt+1))
    return dis

print(min(dijkstra(1)[n]))




# bfs
'''# BFS로 목적지까지 가는 모든 경로 구하기
route = []
Q = deque([(1,[1],"")])
while Q:
    node, r, t = Q.popleft()
    if node == n:
        route.append(t)
        continue
    for x in graph[node]:
        time, next_node = x
        if next_node not in r:
            Q.append((next_node, r+[next_node], t+","+str(time)))

# 모든 경로에서 가장 오래 걸리는 도로들 포장하기
min_value = 10**6
for y in route:
    rt = list(map(int,y[1:].split(",")))
    for _ in range(k):
        rt.pop()
    min_value = min(sum(rt),min_value)

print(min_value)'''
