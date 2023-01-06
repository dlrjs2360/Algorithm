import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

from collections import defaultdict
import heapq

def dijkstra(start,n):
    Q = [(0,start)]
    dis = [1e9] * (n+1)
    dis[start] = 0
    while Q:
        fee, node = heapq.heappop(Q)
        for x in graph[node]:
            nfee, next_node = x
            if nfee+fee < dis[next_node]:
                dis[next_node] = nfee+fee
                Q.append((nfee+fee,next_node))
    return dis

T = int(input())
for _ in range(T):
    n, d, c = map(int,input().split())

    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((s,a))

    hacking= dijkstra(c,n)

    max_value = 0
    count = 0
    for x in hacking:
        if x < 1e9:
            max_value = max(max_value,x)
            count += 1

    print(count,max_value)
