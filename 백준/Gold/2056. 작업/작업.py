import sys
input = sys.stdin.readline
from collections import deque,defaultdict
from heapq import heappop,heappush

n = int(input())
preTask, depth, time = defaultdict(list), [0] * (n+1), [0] * (n+1)

for i in range(1,n+1):
    t, d,*p = map(int, input().split())
    time[i], depth[i], = t,d
    for task in p: preTask[task].append(i)

heap = []
for i in range(1,n+1):
    if depth[i] == 0: heappush(heap,(time[i],i))

t = 0
while heap:
    while heap and t >= heap[0][0]:
        tt, node = heappop(heap)
        for x in preTask[node]:
            depth[x] -= 1
            if depth[x] <= 0: heappush(heap,(t+time[x],x))
    t += 1

print(t-1)