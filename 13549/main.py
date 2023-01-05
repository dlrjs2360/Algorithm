import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path+'/input.txt', "r")

import heapq

n, k = map(int,input().split())
visited = [False] * (10**6+1)
visited[n] = True

heap = [(0,n)]
while heap:
    S,node = heapq.heappop(heap)

    # 정답일 경우
    if node == k:
        print(S)
        break

    # 2배 먼저 처리하기
    doub = node * 2
    if doub < len(visited) and not visited[doub]:
        visited[doub] = True
        heapq.heappush(heap, (S, doub))

    for x in (node + 1, node - 1):
        if 0 <= x < len(visited) and not visited[x]:
            visited[x] = True
            heapq.heappush(heap, (S + 1, x))