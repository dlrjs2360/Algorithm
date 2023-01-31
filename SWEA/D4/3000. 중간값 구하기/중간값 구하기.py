def insert_to_heap(m, v):
    if v < m:
        heapq.heappush(maxheap,-v)
        return
    heapq.heappush(minheap,v)

import heapq
T = int(input())
for test_case in range(1,T+1):
    answer = 0
    n, mid = map(int,input().split())
    maxheap, minheap = [], []

    for i in range(n):
        x,y = map(int,input().split())
        insert_to_heap(mid, x)
        insert_to_heap(mid, y)
        if len(maxheap) > len(minheap):
            heapq.heappush(minheap, mid)
            mid = heapq.heappop(maxheap) * -1
        elif len(maxheap) < len(minheap):
            heapq.heappush(maxheap,-mid)
            mid = heapq.heappop(minheap)
        answer = (answer + mid) % 20171109

    print(f"#{test_case} {answer}")