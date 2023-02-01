import heapq

def insert_heap(val,mid):
    if val < mid:
        heapq.heappush(maxHeap, -val)
        return
    heapq.heappush(minHeap, val)

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = []
    for _ in range(n // 10+1 if n % 10 != 0 else n // 10):
        arr += list(map(int,input().split()))
    maxHeap, minHeap = [], []
    midArr = []
    for i in range(n):
        if i == 0:
            mid = arr[i]
            midArr.append(mid)
            continue
        x = arr[i]
        insert_heap(x, mid)
        if len(maxHeap) > len(minHeap):
            heapq.heappush(minHeap, mid)
            mid = heapq.heappop(maxHeap) * -1
        elif len(maxHeap) < len(minHeap):
            heapq.heappush(maxHeap,-mid)
            mid = heapq.heappop(minHeap)

        if (i-1) % 2 == 1:
            midArr.append(mid)

    print(len(midArr))
    for i in range(len(midArr)):
        print(midArr[i], end = " ")
        if (i+1) % 10 == 0 or (i+1) == len(midArr):
            print()